from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        """
        The ready() method ensures that signals are properly registered when Django starts.
        This is necessary because Django does not automatically load signals.py.
        Without this import, the signal handlers won’t be triggered.
        """
        import users.signals