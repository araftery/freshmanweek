from django.shortcuts import render
from django.views.generic import TemplateView

from core.models import Event
from core.forms import AuditionForm

class HomePageView(TemplateView):

    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['featured_events'] = Event.objects.filter(is_featured=True).order_by('start_time')
        context['audition_form'] = AuditionForm()
        return context


class EventsView(TemplateView):

    template_name = "core/featured-events.html"

    def get_context_data(self, **kwargs):
        context = super(FeaturedEventsView, self).get_context_data(**kwargs)
        context['featured_events'] = Event.objects.filter(is_featured=True).order_by('start_time')
        return context
