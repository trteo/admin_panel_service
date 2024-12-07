from django.db import models

from apps.products.models import Product


class Client(models.Model):
    chat_id = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Client chat id {self.chat_id}"

    class Meta:
        db_table = 'clients'


class CartProducts(models.Model):
    amount = models.PositiveIntegerField()
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='cart'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='cart_items'
    )

    def __str__(self):
        return f"{self.amount} of {self.product.name}"

    class Meta:
        db_table = 'products_in_cart'
