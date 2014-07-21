from django.core.management.base import BaseCommand

from icalendar import Calendar
import requests

from core.models import Event


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
        events = cal.walk('vevents')
        for event in events:
            start_time = event['dtstart'].dt
            end_time = event['dtend'].dt
            name = unicode(event['summary'])
            description = unicode(event['description'])
            location = unicode(event['location'])

            new, created = Event.objects.create(
                name=name,
                location=location,
                description=description,
                start_time=start_time,
                end_time=end_time
            )
