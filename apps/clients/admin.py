from django.contrib import admin

from apps.clients.models import Client, CartProducts


@admin.register(Client)
class UserAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'is_active')
    search_fields = ('chat_id',)
    list_filter = ('is_active',)


@admin.register(CartProducts)
class CartProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'amount')
    search_fields = ('product__name',)
