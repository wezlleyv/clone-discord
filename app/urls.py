from django.urls import path

from .views import *

urlpatterns = [
    path("@me", my_view, name="app"),
    path("<str:_id>/<str:idChannel>", channel_view),
]