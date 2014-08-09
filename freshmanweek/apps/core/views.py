from django.views.generic import TemplateView
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy

from core.models import Event
from talentshow.forms import AuditionForm

class HomePageView(TemplateView):

    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['featured_events'] = Event.objects.filter(is_featured=True).order_by('start_time')
        form = AuditionForm()
        form.helper.form_action = reverse_lazy('talentshow-sign-up')
        context['audition_form'] = form
        return context


class EventsView(TemplateView):

    template_name = "core/events.html"

    def get_context_data(self, **kwargs):
        context = super(EventsView, self).get_context_data(**kwargs)
        context['featured_events'] = Event.objects.filter(is_featured=True).order_by('start_time')
        context['upcoming_events'] = Event.objects.filter(is_featured=False, start_time__gte=timezone.now()).order_by('start_time')[:5]
        return context
