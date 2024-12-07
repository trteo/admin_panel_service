from django.contrib import admin

from apps.faq.models import FAQ


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')
    search_fields = ('question', 'answer')