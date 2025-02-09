# django_signalmap/tracker.py

from django.dispatch import Signal

# Global registry: { signal_name: [receiver_name, ...] }
SIGNAL_MAP = {}

# Save the original connect method of Django’s Signal.
original_connect = Signal.connect

def tracked_connect(self, receiver, sender=None, weak=True, dispatch_uid=None):
    # Call the original connect method to perform the connection.
    result = original_connect(self, receiver, sender, weak, dispatch_uid)
    
    # Use the signal's "name" attribute if set; otherwise, use its repr.
    signal_name = getattr(self, 'name', repr(self))
    
    # Initialize the list for this signal if not already present.
    if signal_name not in SIGNAL_MAP:
        SIGNAL_MAP[signal_name] = []
    
    # Record the receiver's name (or its repr if __name__ isn’t available).
    receiver_name = getattr(receiver, '__name__', repr(receiver))

    # Check to avoid duplicate entries
    if receiver_name not in SIGNAL_MAP[signal_name]:
        SIGNAL_MAP[signal_name].append(receiver_name)
    
    return result

# Monkey-patch: Replace the connect method on all Signal instances.
Signal.connect = tracked_connect
