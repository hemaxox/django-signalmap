# django_signalmap/apps.py

from django.apps import AppConfig

class DjangoSignalMapConfig(AppConfig):
    name = 'django_signalmap'

    def ready(self):
        # Import tracker so that our monkey-patching runs on startup.
        from . import tracker
