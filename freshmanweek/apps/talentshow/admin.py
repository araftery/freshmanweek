from django.contrib import admin

from talentshow.models import Auditioner, AuditionSlot, AuditionSession, AuditionSignUpReminder


class AuditionerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'description', 'auditionslot', 'reminder_email', 'reminder_text', 'time_registered', 'secret')
    ordering = ('time_registered', 'last_name', 'first_name')


class AuditionSlotAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'session', 'duration', 'location', 'auditioner_full_name')
    ordering = ('start_time',)


class AuditionSignUpReminderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_at',)
    ordering = ('created_at',)


admin.site.register(Auditioner, AuditionerAdmin)
admin.site.register(AuditionSlot, AuditionSlotAdmin)
admin.site.register(AuditionSession)
admin.site.register(AuditionSignUpReminder, AuditionSignUpReminderAdmin)