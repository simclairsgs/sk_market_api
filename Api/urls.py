from django.urls import path
from . import views

urlpatterns = [
    path('',views.api,name='api'),
    path('products/', views.product_list, name='list-products'),
    path('products-detail/<str:Id>/', views.product_detail, name='list-detail'),
    path('products-add/', views.product_add, name='add-product'),
    path('products-update/<str:Id>/', views.product_update, name='update-product'),
    path('products-delete/<str:Id>/', views.product_delete, name='delete-product'),

    path('login-adduser/',views.Login_Add_Users,name='login-adduser'),
    path('employees/',views.Employee_list,name='Employee_list'),
    path('employee-delete/<str:ID>/',views.Employee_Delete,name='employee_delete'),
    path('employee-update/<str:Id>/', views.Employee_update, name='employee-product'),


    path('stock-manage/',views.Stock_Manage,name='stock_manage'),
    path('view-onestock/<str:ID>/',views.View_One_Stock,name='view_one_stock'),
    path('view-allstock/',views.View_All_Stock,name='view_all_stock'),
    path('stock-update/<str:Id>/', views.Stock_update, name='stock-update'),


    path('billing-product/',views.Billing_Product,name='billing_product'),
    path('billing-list/',views.Billing_list,name='billing_list'),

    path('total-sales/',views.Total_Sales,name='total_sales'),
    path('get-salesof/<str:date>/',views.Get_Sales_Of,name='get_sales_of'),
    path('get-allsales/',views.Get_All_Sales,name='Get_All_sales'),

]
