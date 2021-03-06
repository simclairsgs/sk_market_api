from django.db import models

# Create your models here.

class Products(models.Model):
    Product_Id = models.CharField(max_length=10, primary_key=True)
    product_Name = models.CharField(max_length=25)
    Description = models.CharField(max_length=40)
    MRP = models.FloatField()
    Price = models.FloatField()
    Stock_Balance = models.IntegerField()
    Discount = models.FloatField()


class Login(models.Model):
    Employee_Id=models.CharField(max_length=10,primary_key=True)
    Employee_Name=models.CharField(max_length=15)
    Mail_Id=models.CharField(max_length=35)
    Date_Of_Birth=models.CharField(max_length=12)
    Mobile_Number=models.CharField(max_length=15)
    Address=models.CharField(max_length=40)
    Password=models.CharField(max_length=15)
    Status=models.BooleanField(default=False)
    Date_Of_Joining=models.CharField(max_length=25)


class Stock(models.Model):
    Product_Name=models.CharField(max_length=25)
    Product_Id=models.CharField(max_length=10, primary_key=True)
    Dealer_Mail_Id=models.EmailField()
    Order_quantity=models.IntegerField()


class Sales(models.Model):
    Date=models.CharField(max_length=12)
    Sales=models.FloatField()

    
class Billing(models.Model):
    Bill_No=models.IntegerField()
    Timestamp=models.CharField(max_length=30)
    Products=models.CharField(max_length=1000)
    Product_Count=models.IntegerField()
    Amount=models.FloatField()
    Billing_Employee=models.CharField(max_length=25)


class Tax(models.Model):
    Tax_Date=models.CharField(max_length=20,default='0.00')
    Tax_Amount=models.CharField(max_length=20)
    
