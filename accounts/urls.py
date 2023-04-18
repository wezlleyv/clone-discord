from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path("register/", register, name="register"),
]