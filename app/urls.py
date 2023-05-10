from django.urls import path

from .views import *

urlpatterns = [
    path("@me", app_view, name="app"),
    path('createserver', create_server_view),
    path("invite/<int:serverId>", invite_server_view),
    path("<str:_id>/<str:idChannel>", channel_view),
    path("<str:_id>", redirect_view),
]