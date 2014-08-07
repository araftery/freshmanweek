from django.conf import settings


def debug(request):
    "Returns context variables helpful for debugging."
    context_extras = {}
    if settings.DEBUG:
        context_extras['debug'] = True
    return context_extras