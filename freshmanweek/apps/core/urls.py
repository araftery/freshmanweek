from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from core.views import HomePageView, EventsView

urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name="core-home"),
    url(r'^events/$', EventsView.as_view(),  name="events"),
    url(r'^tours/$', TemplateView.as_view(template_name="core/tours.html"), name="tours"),
)