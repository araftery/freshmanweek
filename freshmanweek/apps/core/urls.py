from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from core.views import HomePageView, FeaturedEventsView

urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name="core-home"),
    url(r'^events/$', FeaturedEventsView.as_view(),  name="events"),
)