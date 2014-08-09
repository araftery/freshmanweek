from django.http import Http404, HttpResponseNotAllowed
from django.core.urlresolvers import reverse
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, UpdateView
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from django.utils.timezone import now

from core.mixins import AjaxFormViewMixin
from core.tasks import send_email
from core.utils.general import is_freshmanweek
from talentshow.forms import AuditionForm, ChooseAuditionSlotForm, AuditionReminderForm
from talentshow.models import Auditioner, AuditionSession


class SetAuditionReminderView(AjaxFormViewMixin, UpdateView):
    form = AuditionReminderForm
    model = Auditioner

    def valid_response(self, form):
        response = super(SetAuditionReminderView, self).valid_response(form)
        response.update({
            'reminder_text': form.cleaned_data.get('reminder_text'),
            'reminder_email': form.cleaned_data.get('reminder_email'),
        })
        return response

    def get_form(self, form_class):
        """
        This is hacky
        """
        data = model_to_dict(self.object)
        data['reminder_text'] = self.request.POST.get('reminder_text')
        data['reminder_email'] = self.request.POST.get('reminder_email')
        return form_class(instance=self.object, data=data)

    def get_object(self):
        secret = self.request.POST.get('secret')
        if not secret or not is_freshmanweek():
            raise Http404
        return get_object_or_404(Auditioner, secret=secret)


class AuditionerSignUpView(CreateView):
    model = Auditioner
    form_class = AuditionForm
    template_name = 'talentshow/sign-up.html'

    def post(self, request, *args, **kwargs):
        if not is_freshmanweek():
            return HttpResponseNotAllowed(['GET'])
        return super(AuditionerSignUpView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        success_url = reverse('talentshow-choose-slot', kwargs={'secret': self.object.secret})
        return success_url


class ChooseAuditionSlotView(FormView):
    form_class = ChooseAuditionSlotForm
    template_name = 'talentshow/choose-slot.html'


    def get_context_data(self, **kwargs):
        context = super(ChooseAuditionSlotView, self).get_context_data(**kwargs)
        sessions = list(AuditionSession.objects.all())
        for session in sessions:
            if now() > session.last_time or not session.remaining_slots_exist:
                sessions.remove(session)
        sessions.sort(key=lambda x: x.start_time)
        for session in sessions:
            session.slots = session.auditionslot_set.filter(start_time__gte=now(), auditioner=None).order_by('start_time')
        context['sessions'] = sessions
        return context

    def get(self, request, *args, **kwargs):
        """
        Check the secret, make sure it corresponds to an auditioner who doesn't have a
        slot yet.
        """
        secret = self.kwargs.get('secret')
        if not secret or not Auditioner.objects.filter(secret=secret).exists() or not is_freshmanweek():
            raise Http404

        if Auditioner.objects.filter(secret=secret).exclude(auditionslot=None).exists():
            person = Auditioner.objects.filter(secret=secret).exclude(auditionslot=None)[0]
            return render(self.request, 'talentshow/sign-up-success.html', {'slot': person.auditionslot, 'auditioner': person})
            #return redirect('talentshow-cannot-change-slot')

        return super(ChooseAuditionSlotView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Check the secret, make sure it corresponds to an auditioner who doesn't have a
        slot yet.
        """
        secret = self.kwargs.get('secret')
        if not secret or not Auditioner.objects.filter(secret=secret).exists() or not is_freshmanweek():
            raise Http404

        if Auditioner.objects.filter(secret=secret).exclude(auditionslot=None).exists():
            return redirect('talentshow-cannot-change-slot')

        return super(ChooseAuditionSlotView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        slot = form.cleaned_data.get('audition_slot')
        secret = self.kwargs.get('secret')
        auditioner = Auditioner.objects.get(secret=secret)
        slot.auditioner = auditioner
        slot.save()

        send_email.delay(
            template_name='audition_confirm',
            subject='Talent Show Audition Confirmation',
            from_email=settings.HARVARD_TALENT_EMAIL,
            recipients=[slot.auditioner.email],
            context={'slot': slot}
        )

        reminder_form = AuditionReminderForm(instance=auditioner)
        if not auditioner.phone:
            reminder_form.fields.pop('reminder_text')

        return render(self.request, 'talentshow/sign-up-success.html', {'slot': slot, 'auditioner': auditioner, 'reminder_form': reminder_form})


