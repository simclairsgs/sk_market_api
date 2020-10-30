from django.contrib import admin
from .models import Products

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['Product_Id', 'product_Name', 'Description', 'MRP' , 'Price', 'Stock_Balance' ,'Discount']


admin.site.register(Products, ProductsAdmin)