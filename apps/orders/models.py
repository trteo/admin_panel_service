from django.db import models

from apps.products.models import Product
from apps.clients.models import Client


class Order(models.Model):
    STATUS_CHOICES = [
        ("registered", "Зарегистрирован"),
        ("paid", "Оплачен"),
        ("delivered", "Доставлен"),
    ]
    delivery_address = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)

    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='orders'
    )

    def __str__(self):
        return f"Order {self.id} for {self.client}"

    class Meta:
        db_table = 'orders'


class OrderProducts(models.Model):
    amount = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='order_items'
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='ordered_products'
    )

    def __str__(self):
        return f"{self.amount} of {self.product.name}"

    class Meta:
        db_table = 'products_in_order'
