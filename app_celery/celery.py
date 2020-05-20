import os
import smtplib

from celery import Celery
from celery.schedules import crontab
from django.core.mail import send_mail
from django.http import HttpResponse

from django.conf import settings
from django.template.loader import render_to_string


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "umschool.settings")
app = Celery('umschool', broker=settings.CELERY_BROKER_URL)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()



def hello(request):
    test("vfvdfvd")
    return HttpResponse()


@app.task
def test(arg):
    from django.core.mail import send_mail
    from django.conf import settings
    from user.models import User
    import smtplib
    print(arg)

    print(User.objects.values_list("email", flat=True))
    send_mail(subject="Новый день", message="Пора решать новые задачки", from_email=settings.DEFAULT_FROM_EMAIL,recipient_list=User.objects.values_list("email", flat=True))
    # except smtplib.SMPTException:
    #     print(f'Error while sending email ')


@app.task
def send_email(subject, from_email, to_email, template, args):
    print(from_email)
    html_message = render_to_string(template, args)
    print(to_email)
    try:
      send_mail(subject=subject, message='', from_email=from_email,recipient_list=[to_email], html_message=html_message)
    except smtplib.SMPTException:
        print(f'Error while sending email to {to_email}')


