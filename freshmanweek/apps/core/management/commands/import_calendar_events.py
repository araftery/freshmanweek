import datetime
from icalendar import Calendar
import requests
import pytz

from django.core.management.base import BaseCommand
from django.db.utils import DataError
from django.conf import settings

from core.models import Event

timezone = pytz.timezone(settings.TIME_ZONE)
MAX_DESCRIPTION_LENGTH = 450

def smart_truncate(content, length=100, suffix='...'):
    if len(content) <= length:
        return content
    else:
        return ' '.join(content[:length+1].split(' ')[0:-1]) + suffix

class Command(BaseCommand):
    """
    Command to import calendar events as Events.

    Note: destructive. Will replace all ics events.
    """
    help = 'Import and replace calendar events.'

    def handle(self, *args, **options):
        url = args[0]
        cal_data = requests.get(url).content
        cal = Calendar().from_ical(cal_data)
        events = cal.walk('vevent')
        Event.objects.filter(from_ics=True).delete()
        for event in events:
            end_time = event.get('dtend')
            if not end_time or not isinstance(end_time.dt, datetime.datetime):
                continue
            start_time = event.get('dtstart').dt.replace(year=2014)
            end_time = event.get('dtend').dt.replace(year=2014)
            name = event.get('summary')
            description = event.get('description')
            location = event.get('location')

            if description:
                description = smart_truncate(description, MAX_DESCRIPTION_LENGTH)

            new = Event.objects.create(
                name=unicode(name),
                location=unicode(location) if location else None,
                description=unicode(description) if description else None,
                start_time=start_time,
                end_time=end_time,
                is_featured=False,
                from_ics=True,
            )
