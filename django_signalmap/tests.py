import unittest
from django.dispatch import Signal
from django_signalmap.tracker import SIGNAL_MAP

# Dummy receiver functions for testing
def dummy_receiver(sender, **kwargs):
    pass

class DummyReceiver:
    @staticmethod
    def handle(sender, **kwargs):
        pass

class DjangoSignalMapTestCase(unittest.TestCase):
    def setUp(self):
        # Clear the global SIGNAL_MAP before each test
        SIGNAL_MAP.clear()

    def test_single_receiver_registration(self):
        # Create a dummy signal and set a custom name for clarity
        dummy_signal = Signal()
        dummy_signal.name = "dummy_signal"
        
        # Connect the dummy receiver
        dummy_signal.connect(dummy_receiver)
        
        # Check that the signal's name appears in SIGNAL_MAP and contains the receiver's name
        self.assertIn("dummy_signal", SIGNAL_MAP)
        self.assertIn("dummy_receiver", SIGNAL_MAP["dummy_signal"])
        self.assertEqual(len(SIGNAL_MAP["dummy_signal"]), 1)

    def test_multiple_receivers_registration(self):
        dummy_signal = Signal()
        dummy_signal.name = "dummy_signal"
        
        # Connect two different receivers
        dummy_signal.connect(dummy_receiver)
        dummy_signal.connect(DummyReceiver.handle)
        
        self.assertIn("dummy_signal", SIGNAL_MAP)
        self.assertIn("dummy_receiver", SIGNAL_MAP["dummy_signal"])
        self.assertIn("handle", SIGNAL_MAP["dummy_signal"])
        self.assertEqual(len(SIGNAL_MAP["dummy_signal"]), 2)

    def test_duplicate_receiver_registration(self):
        dummy_signal = Signal()
        dummy_signal.name = "dummy_signal"
        
        # Connect the same receiver twice
        dummy_signal.connect(dummy_receiver)
        dummy_signal.connect(dummy_receiver)
        
        self.assertIn("dummy_signal", SIGNAL_MAP)
        # With deduplication, the same receiver should only appear once.
        self.assertEqual(len(SIGNAL_MAP["dummy_signal"]), 1)

if __name__ == "__main__":
    unittest.main()
