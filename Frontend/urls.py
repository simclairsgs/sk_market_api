from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='frontend_index'),
    path('home', views.home,name='home'),
    path('register', views.register,name='register'),
    path('billing', views.billing,name='billing'),
    path('products-enq', views.penq,name='product-enq'),
    path('stock-enq', views.senq,name='stock-enq'),
    path('change-password', views.change_pass,name='change_pass'),
    path('forgot-password', views.forgot_pass,name='forgot_pass'),
]
