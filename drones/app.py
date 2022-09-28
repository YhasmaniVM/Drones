from django.apps import AppConfig
from django.conf import settings


class CheckBatteryConfig(AppConfig):
    name = 'check_drones_battery'

    def ready(self):
        from . import scheduler
        if settings.SCHEDULER_AUTOSTART:
            scheduler.start()
