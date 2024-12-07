from django.contrib import admin

from apps.products.models import ProductCategory, Product


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent_category')
    search_fields = ('id', 'name',)
    list_filter = ('parent_category',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description', 'price', 'image')
    search_fields = ('id', 'name', 'category')
    list_filter = ('category',)
    list_editable = ('name', 'category', 'description', 'price', 'image')
