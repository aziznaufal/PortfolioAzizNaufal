from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('app/', views.post_list, name='post_list'),
    path('rsa_encryption/', views.encrypt_message, name='encrypt_message'),
]
