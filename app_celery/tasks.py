from celery.schedules import crontab
from umschool import settings

from app_celery.celery import app,test
app.autodiscover_tasks()

@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute='*/1'), test.s("asdfghj"))