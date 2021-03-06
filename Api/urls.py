from django.urls import path
from . import views

views.tax_mgmt()

urlpatterns = [
    # Login Authentication 
    path('login-auth/',views.login_auth,name='login_auth'),
    path('register-user/',views.register_user,name='register_user'),
    path('change-password/',views.change_password,name="change_password"),
    path('forgot-password/',views.forgot_password,name="forgot_password"),

    # Products data api
    path('products/', views.product_list, name='list-products'),
    path('products-detail/<str:Id>/', views.product_detail, name='list-detail'),
    path('products-add/', views.product_add, name='add-product'),
    path('products-update/<str:Id>/', views.product_update, name='update-product'),
    path('products-delete/<str:Id>/', views.product_delete, name='delete-product'),
    path('products-namelist', views.product_namelist, name='Pname_autocomplete'),
    path('products-idlist', views.product_idlist, name='Pid_autocomplete'),

    # Employee/Login data api
    path('employee-addnew/',views.login_add_users,name='login-adduser'),
    path('employees/<str:Id>/',views.employee_list,name='Employee_list'),
    path('employee-delete/<str:Id>/',views.employee_delete,name='employee_delete'),
    path('employee-update/<str:Id>/', views.employee_update, name='employee-product'),
    

    # stock data api
    path('stock-add-data/',views.stock_add_detail,name='stock_manage'),
    path('view-onestock/<str:Id>/',views.view_one_stock,name='view_one_stock'),
    path('view-allstock/',views.view_all_stock,name='view_all_stock'),
    path('stock-update/<str:Id>/', views.stock_update, name='stock-update'),
    path('reduce-stock/',views.reduce_stock,name='reduce-stock'),

    # billing data api
    path('billing-product/',views.billing_product,name='billing_product'),
    path('billing-list/',views.billing_list,name='billing_list'),
    path('create-billnum',views.create_billnum,name='create-billnum'),
    path('getproduct-detailsname/<str:Name>/',views.get_product_detils_name,name='get_product_detils_name'),

    #sales data api
    path('total-sales/',views.total_sales,name='total_sales'),
    path('get-salesof/<str:date>/',views.get_sales_of,name='get_sales_of'),
    path('get-allsales/',views.get_all_sales,name='Get_All_sales'),
    path('sales-add/',views.sales_add,name='sales_add'),

    #tax data api
    path('add-tax/',views.add_tax,name='add-tax'),
    path('get-alltax/',views.get_all_tax,name='get-alltax'),
    path('get-taxof/<str:date>/',views.get_tax_of,name='get_taxof'),

]
