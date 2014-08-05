from django.contrib import admin
from django import forms

from core.models import Event

class EventAdminForm(forms.ModelForm):
    description = forms.CharField(max_length=2000, widget=forms.Textarea)

    class Meta:
        model = Event


class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm
    list_display = ('name', 'description', 'location', 'start_time', 'end_time', 'is_featured', 'extra_info')
    ordering = ('is_featured', 'start_time', 'name')

admin.site.register(Event, EventAdmin)
