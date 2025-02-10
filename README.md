# Django SignalMap

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/django-signalmap.svg)](https://pypi.org/project/django-signalmap/)

Django SignalMap is a lightweight Django package that automatically tracks, maps, and visualizes the signal connections in your Django project. By monkey-patching Django's signal connect method, SignalMap records which receivers are attached to each signal and provides a management command to display this map in an easy-to-read format.

## Features

- **Automatic Signal Tracking:**  
  Records all signal registrations across your project without any manual configuration.

- **Management Command:**  
  Run `python manage.py signalmap` to print a detailed overview of signals and their connected receiver functions.

- **Custom Signal Names:**  
  Easily assign friendly names to your custom signals for better readability in the output.

- **Lightweight & Non-Intrusive:**  
  Designed to work in development mode without affecting production performance.

- **Open Source & Community-Driven:**  
  Contributions, improvements, and feedback are welcome!

## Installation

1. **Install via pip:**

   ```bash
   pip install django-signalmap
   ```

2. **Add to your INSTALLED_APPS:**

   In your project's settings.py, add the following line:

   ```python
   INSTALLED_APPS = [
       # ... other installed apps ...
       'django_signalmap.apps.DjangoSignalMapConfig',
   ]
   ```

## Usage

### Registering Signals

Ensure that your app's signals are imported so that they are registered. For example, in your app's apps.py:

```python
# myapp/apps.py
from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        # Import the signals module to register signals
        import myapp.signals
```

### Example Signal

Create a signals.py file in your app (e.g., myapp/signals.py):

```python
# myapp/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved(sender, instance, **kwargs):
    print("User saved!")
```

### Viewing the Signal Map

After your signals are registered (for example, after running your server or a shell session), run:

```bash
python manage.py signalmap
```

You should see output similar to:

```
Signal: <django.dispatch.dispatcher.Signal object at 0x...>
  -> Receiver: user_saved
```

## Testing

To better see the results, you can add additional custom signals and receivers to your signals.py file:

```python
from django.dispatch import Signal, receiver

# Custom signal (providing_args is no longer required in Django 3.1+)
order_processed = Signal()
order_processed.name = "order_processed"

@receiver(order_processed)
def notify_customer(sender, order_id, status, **kwargs):
    print(f"Notify customer: Order {order_id} is now {status}.")

@receiver(order_processed)
def update_inventory(sender, order_id, status, **kwargs):
    print(f"Update inventory for Order {order_id} after status {status}.")

# Another custom signal for testing purposes
data_imported = Signal()
data_imported.name = "data_imported"

@receiver(data_imported)
def log_import(sender, data_source, **kwargs):
    print(f"Data imported from {data_source}.")
```

Then trigger the signals in a Django shell:

```bash
python manage.py shell
```

Within the shell, run:

```python
from myapp.signals import order_processed, data_imported
order_processed.send(sender=None, order_id=1234, status='processed')
data_imported.send(sender=None, data_source='CSV file')
```

And run the management command again:

```bash
python manage.py signalmap
```

## Contributing

Contributions are welcome! If you have suggestions, bug fixes, or improvements, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes.
4. Push your branch.
5. Open a pull request on GitHub.

For any issues or feature requests, please open an issue in the GitHub repository.

## License

This project is licensed under the MIT License.

## Contact

For questions, suggestions, or support, please contact ibrahim.muhaisen.2015@gmail.com.

Happy coding!
