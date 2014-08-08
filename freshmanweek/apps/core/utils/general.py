import datetime
import pytz

from django.conf import settings


tz = pytz.timezone(settings.TIME_ZONE)

def is_freshmanweek():
    if hasattr(settings, 'is_fwk'):
        return settings.is_fwk
    else:
        fwk_start = datetime.datetime(*settings.FWK_START_DATE)
        now = datetime.datetime.now()
        return now >= fwk_start
