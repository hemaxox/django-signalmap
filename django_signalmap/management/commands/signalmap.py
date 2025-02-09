# django_signalmap/management/commands/signalmap.py

from django.core.management.base import BaseCommand
from django_signalmap.tracker import SIGNAL_MAP

class Command(BaseCommand):
    help = 'Prints a map of Django signals and their connected receivers.'

    def handle(self, *args, **options):
        if not SIGNAL_MAP:
            self.stdout.write("No signal connections have been tracked yet.")
            return
        
        for signal, receivers in SIGNAL_MAP.items():
            self.stdout.write(f"Signal: {signal}")
            for receiver in receivers:
                self.stdout.write(f"  -> Receiver: {receiver}")
            self.stdout.write("")
