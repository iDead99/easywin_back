from django.apps import AppConfig


class ManageEasywinConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'manage_easywin'

    def ready(self) -> None:
         import manage_easywin.signals
