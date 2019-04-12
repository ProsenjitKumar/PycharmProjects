from django.contrib import admin
from .models import ProductCategory, Product


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_per_page = 10
    search_fields = ['title']


admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'created', 'updated']
    list_per_page = 10
    search_fields = ['name', 'category', 'price', 'created', 'updated']


admin.site.register(Product, ProductAdmin)