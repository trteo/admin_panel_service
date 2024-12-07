from django.contrib import admin

from apps.mailing.models import Mailing


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'sending_date', 'is_sent')
    search_fields = ('message_text',)
    list_filter = ('is_sent', 'sending_date')
