from django.conf.urls import patterns, url

from talentshow.views import AuditionerSignUpView, ChooseAuditionSlotView, SetAuditionReminderView

urlpatterns = patterns('',
    url(r'^$', AuditionerSignUpView.as_view(), name="talentshow-sign-up"),
    url(r'^choose-slot/(?P<secret>\w+)/$', ChooseAuditionSlotView.as_view(), name="talentshow-choose-slot"),
    url(r'^set-reminder/$', SetAuditionReminderView.as_view(), name="talentshow-set-reminder"),
)
