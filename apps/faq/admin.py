from django.contrib import admin

from apps.faq.models import FAQ


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer')
    search_fields = ('question', 'answer')