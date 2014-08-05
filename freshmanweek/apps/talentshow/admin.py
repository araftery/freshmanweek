from django.contrib import admin

from talentshow.models import Auditioner, AuditionSlot, AuditionSession


class AuditionerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'description', 'auditionslot', 'reminder_email', 'reminder_text', 'time_registered', 'secret')
    ordering = ('time_registered', 'last_name', 'first_name')


class AuditionSlotAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'session', 'duration', 'location', 'auditioner_full_name')
    ordering = ('start_time',)

admin.site.register(Auditioner, AuditionerAdmin)
admin.site.register(AuditionSlot, AuditionSlotAdmin)
admin.site.register(AuditionSession)