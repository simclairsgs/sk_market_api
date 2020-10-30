from django.urls import path
from . import views

urlpatterns = [
    path('',views.api,name='api'),
    path('products/', views.product_list, name='list-products'),
    path('products-detail/<str:Id>/', views.product_detail, name='list-detail'),
    path('products-add/', views.product_add, name='add-product'),
    path('products-update/<str:Id>/', views.product_update, name='update-product'),
    path('products-delete/<str:Id>/', views.product_delete, name='delete-product'),
   
]
