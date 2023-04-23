from django.db import models

# Create your models here.
class Server(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="server/", default="default.jpeg")

    def __str__(self):
        return self.name


class Channels(models.Model):
    ID = models.AutoField(primary_key=True)
    id_to_server = models.IntegerField()
    icon = models.CharField(default="static/images/iconsCH/hastag.png", max_length=1000)
    name = models.CharField(max_length=30)