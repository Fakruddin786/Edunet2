from django.urls import path
from .views import index , about , register , login

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('register', register, name='register'),
    path('login', login, name='login'),  
]     