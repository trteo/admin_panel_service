from django.db import models

from apps.products.models import Product


class Client(models.Model):
    chat_id = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Client chat id {self.chat_id}"


class CartProducts(models.Model):
    amount = models.PositiveIntegerField()
    chat = models.ForeignKey(
        Client, to_field='chat_id', on_delete=models.CASCADE, related_name='user_cart'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='cart_items'
    )

    def __str__(self):
        return f"{self.amount} of {self.product.name}"
