from django.urls import path
from . import views

urlpatterns = [
    # Login Authentication 
    path('login-auth/',views.login_auth,name='login_auth'),
    path('register-user/',views.register_user,name='register_user'),
    path('change-password/',views.change_password,name="change_password"),
    path('forgot-password/',views.forgot_password,name="forgot_password"),

    # Products data api
    path('',views.api,name='api'),
    path('products/', views.product_list, name='list-products'),
    path('products-detail/<str:Id>/', views.product_detail, name='list-detail'),
    path('products-add/', views.product_add, name='add-product'),
    path('products-update/<str:Id>/', views.product_update, name='update-product'),
    path('products-delete/<str:Id>/', views.product_delete, name='delete-product'),

    # Employee/Login data api
    path('employee-addnew/',views.login_add_users,name='login-adduser'),
    path('employees/',views.employee_list,name='Employee_list'),
    path('employee-delete/<str:Id>/',views.employee_delete,name='employee_delete'),
    path('employee-update/<str:Id>/', views.employee_update, name='employee-product'),
    

    # stock data api
    path('stock-add-data/',views.stock_add_detail,name='stock_manage'),
    path('view-onestock/<str:Id>/',views.view_one_stock,name='view_one_stock'),
    path('view-allstock/',views.view_all_stock,name='view_all_stock'),
    path('stock-update/<str:Id>/', views.stock_update, name='stock-update'),

    # billing data api
    path('billing-product/',views.billing_product,name='billing_product'),
    path('billing-list/',views.billing_list,name='billing_list'),

    #sales data api
    path('total-sales/',views.total_sales,name='total_sales'),
    path('get-salesof/<str:date>/',views.get_sales_of,name='get_sales_of'),
    path('get-allsales/',views.get_all_sales,name='Get_All_sales'),

]
