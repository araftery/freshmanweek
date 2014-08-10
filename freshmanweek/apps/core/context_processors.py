from django.conf import settings
from django.contrib.sites.models import Site

from core.utils.general import is_freshmanweek


site = Site.objects.get_current()


def debug(request):
    "Returns context variables helpful for debugging."
    context_extras = {}
    if settings.DEBUG:
        context_extras['debug'] = True
    return context_extras

def is_it_freshmanweek(request):
    """
    Returns var is_fwk which is True during FWK
    """
    return {'is_fwk': is_freshmanweek()}

def site_url(request):
    """
    Returns the current site url to the context
    """
    return {'SITE_URL': u'http://{}'.format(site.domain)}
