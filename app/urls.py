from django.urls import path

from .views import *

urlpatterns = [
    path("", my_view, name="app")
]