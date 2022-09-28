import logging

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor
from django_apscheduler.jobstores import register_events, register_job
from .models import Drones
from django.conf import settings

# Create scheduler to run in a thread inside the application process
scheduler = BackgroundScheduler(settings.SCHEDULER_CONFIG)


def check_drones_battery(self):
    for drones in Drones.objects.raw('SELECT battery FROM Drones'):
        print("Battery lv" + drones)

# FIXME doesnt start scheduler process
def start():
    if settings.DEBUG:
      	# Hook into the apscheduler logger
        logging.basicConfig()
        logging.getLogger('apscheduler').setLevel(logging.DEBUG)

    # Adding this job here instead of to crons.
    # This will do the following:
    # - Add a scheduled job to the job store on application initialization
    # - The job will execute a model class method at midnight each day
    # - replace_existing in combination with the unique ID prevents duplicate copies of the job
    scheduler.add_job(check_drones_battery, "cron", id="check_drones_battery_job", minutes=1, replace_existing=True)

    # Add the scheduled jobs to the Django admin interface
    register_events(scheduler)
    register_job(scheduler)
    scheduler.start()
