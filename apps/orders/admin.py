from django.contrib import admin

from apps.orders.models import OrderProducts, Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'delivery_address', 'date_created', 'status')
    search_fields = ('id', 'client__chat_id', 'date_created')
    list_filter = ('date_created',)


@admin.register(OrderProducts)
class OrderProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'order', 'amount', 'price')
    search_fields = ('product__name', 'order__id')
