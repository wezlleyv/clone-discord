from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Server)
admin.site.register(Channels)
admin.site.register(Message)