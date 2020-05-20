import smtplib
from app_celery.celery import app

from django.core.mail import send_mail
from django.template.loader import render_to_string


