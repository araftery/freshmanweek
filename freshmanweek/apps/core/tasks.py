import datetime, logging

from django.conf import settings
from django.utils import timezone

from celery.task import task

from core.utils.general import send_html_email
from core.utils.general import send_text as send_text_utility
from talentshow.models import Auditioner
from celery.task.schedules import crontab
from celery.decorators import periodic_task

logger = logging.getLogger(__name__)


@task
def send_email(template_name, subject, from_email, recipients, context):
    logger.info('Sending {} email to {}'.format(template_name, from_email))
    return send_html_email(template_name, subject, from_email, recipients, context)

@task
def send_text(template_name, recipient, context):
    logger.info('Sending {} text to {}'.format(template_name, recipient))
    return send_text_utility(template_name, recipient, context)

@periodic_task(run_every=crontab(hour="*/2", minute=0))
def send_reminder_chooseslot_emails():
    four_hours_ago = timezone.now() - datetime.timedelta(hours=4)
    auditioners = Auditioner.objects.filter(
        time_registered__lte=four_hours_ago,
        auditionslot=None,
        sent_slot_reminder_email=False
    )
    for auditioner in auditioners:
        send_email.delay(
            template_name='auditionslot_signup_reminder',
            subject='Reminder: Choose an audition slot',
            from_email=settings.HARVARD_TALENT_EMAIL,
            recipients=[auditioner.email],
            context={'auditioner': auditioner},
        )
        auditioner.sent_slot_reminder_email = True
        auditioner.save()

@periodic_task(run_every=crontab(hour=19, minute=0))
def send_reminder_emails():
    tomorrow = timezone.now().date() + datetime.timedelta(1)
    next_day = tomorrow + datetime.timedelta(1)
    tomorrow_start = datetime.datetime.combine(tomorrow, datetime.time())
    tomorrow_end = datetime.datetime.combine(next_day, datetime.time())

    # get all of tomorrow's auditioners who asked for email
    # reminders
    auditioners = Auditioner.objects.filter(
        reminder_email=True,
        sent_reminder_email=False,
        auditionslot__start_time__gte=tomorrow_start,
        auditionslot__start_time__lte=tomorrow_end,
    )
    for auditioner in auditioners:
        send_email.delay(
            template_name='audition_reminder',
            subject='Reminder: Talent show audition tomorrow',
            from_email=settings.HARVARD_TALENT_EMAIL,
            recipients=[auditioner.email],
            context={'auditioner': auditioner},
        )
        auditioner.sent_reminder_email = True
        auditioner.save()


@periodic_task(run_every=crontab(hour="*/2", minute=0))
def send_reminder_texts():
    now = timezone.now()
    four_hours_ahead = now + datetime.timedelta(hours=4)

    # get all auditioners who want a reminder text, haven't yet been
    # sent one, and are auditioning within the next 4 hours
    auditioners = Auditioner.objects.filter(
        reminder_text=True,
        sent_reminder_text=False,
        auditionslot__start_time__gte=now,
        auditionslot__start_time__lte=four_hours_ahead,
    ).exclude(
        phone=None,
    )
    for auditioner in auditioners:
        send_text.delay(
            template_name='audition_reminder',
            recipient=auditioner.phone,
            context={'auditioner': auditioner},
        )
        auditioner.sent_reminder_text = True
        auditioner.save()
