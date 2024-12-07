from django.apps import AppConfig


class FaqConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.faq'

    verbose_name = "FAQ"
    verbose_name_plural = "FAQ"
