from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    parent_category = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subcategories'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product_categories'


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='static_content/product_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, related_name='products'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'
