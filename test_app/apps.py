from django.apps import AppConfig

class TestAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "test_app"

    def ready(self):
        # Import the signals module to ensure signal registration happens
        import test_app.signals