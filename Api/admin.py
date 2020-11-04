from django.contrib import admin
from .models import Products,Login,Sales,Stock,Billing,Tax

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['Product_Id', 'product_Name', 'Description', 'MRP' , 'Price', 'Stock_Balance' ,'Discount']



class LoginAdmin(admin.ModelAdmin):
    list_display = ['Employee_Id','Employee_Name','Mail_Id','Date_Of_Birth','Mobile_Number','Address','Password','Status','Date_Of_Joining']



class SalesAdmin(admin.ModelAdmin):
    list_display = ['Date','Sales']



class StockAdmin(admin.ModelAdmin):
    list_display = ['Product_Name','Product_Id','Dealer_Mail_Id','Order_quantity']


class BillingAdmin(admin.ModelAdmin):
    list_display = ['Bill_No','Timestamp','Products','Product_Count', 'Amount', 'Billing_Employee']

class TaxAdmin(admin.ModelAdmin):
    list_display=['Tax_Date','Tax_Amount']

admin.site.register(Products, ProductsAdmin)
admin.site.register(Login,LoginAdmin)
admin.site.register(Sales,SalesAdmin)
admin.site.register(Stock,StockAdmin)
admin.site.register(Billing,BillingAdmin)
admin.site.register(Tax,TaxAdmin)