from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='frontend_index'),
    path('home', views.home,name='home'),
    path('register', views.register,name='register'),
]
