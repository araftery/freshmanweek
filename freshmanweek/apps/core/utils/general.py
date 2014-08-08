import datetime
import pytz

from django.conf import settings


tz = pytz.timezone(settings.TIME_ZONE)

def is_freshmanweek():
    if hasattr(settings, 'IS_FWK'):
        return settings.IS_FWK
    else:
        fwk_start = datetime.datetime(*settings.FWK_START_DATE)
        now = datetime.datetime.now()
        return now >= fwk_start
