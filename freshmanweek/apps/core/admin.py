from django.contrib import admin
from django import forms

from core.models import Event, FeaturedEvent

class EventAdminForm(forms.ModelForm):
    description = forms.CharField(max_length=2000, widget=forms.Textarea)

    class Meta:
        model = Event


class FeaturedEventAdminForm(EventAdminForm):
    def __init__(self, *args, **kwargs):
        super(FeaturedEventAdminForm, self).__init__(*args, **kwargs)
        print dir(self)
        print self.fields
        print self.base_fields
        print self.data
        print self.initial
        print self.instance

    class Meta:
        model = FeaturedEvent


class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm
    list_display = ('name', 'description', 'location', 'start_time', 'end_time', 'is_featured', 'extra_info')
    ordering = ('is_featured', 'start_time', 'name')
    search_fields = ('name', 'start_time', 'is_featured')


class FeaturedEventAdmin(EventAdmin):
    form = FeaturedEventAdminForm
    list_display = ('name', 'description', 'location', 'start_time', 'end_time')
    ordering = ('start_time', 'name')
    readonly_fields = ('is_featured', 'from_ics',)

    def queryset(self, request):
        qs = super(FeaturedEventAdmin, self).queryset(request)
        qs = qs.filter(is_featured=True)
        return qs



admin.site.register(Event, EventAdmin)
admin.site.register(FeaturedEvent, FeaturedEventAdmin)