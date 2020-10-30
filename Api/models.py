from django.db import models

# Create your models here.

class Products(models.Model):
    Product_Id = models.CharField(max_length=10, primary_key=True)
    product_Name = models.CharField(max_length=20)
    Description = models.CharField(max_length=40)
    MRP = models.FloatField()
    Price = models.FloatField()
    Stock_Balance = models.IntegerField()
    Discount = models.FloatField()