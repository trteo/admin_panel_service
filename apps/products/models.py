from django.db import models


class ProductCategory(models.Model):
    """
    id: int
    name: text

    parent category id: FK(self)
    """
    ...


class Product(models.Model):
    """
    id: int
    name: str
    description: str
    image: str

    category id: FK
    """

