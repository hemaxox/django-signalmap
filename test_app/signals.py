# test_app/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from django.contrib.auth.models import User

# Existing signal example: When a User is saved.
@receiver(post_save, sender=User)
def user_saved(sender, instance, **kwargs):
    print("User saved!")

# -----------------------------
# Additional Testing Signals
# -----------------------------

# Define a custom signal for order processing.
order_processed = Signal()
order_processed.name = "order_processed"  # Set a friendly name.

# First receiver for order_processed.
@receiver(order_processed)
def notify_customer(sender, order_id, status, **kwargs):
    print(f"Notify customer: Order {order_id} is now {status}.")

# Second receiver for order_processed.
@receiver(order_processed)
def update_inventory(sender, order_id, status, **kwargs):
    print(f"Update inventory for Order {order_id} after status {status}.")

# Define another custom signal for testing.
order_processed = Signal()
order_processed.name = "data_imported"

# Receiver for data_imported.
@receiver(order_processed)
def log_import(sender, data_source, **kwargs):
    print(f"Data imported from {data_source}.")
