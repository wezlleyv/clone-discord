# Generated by Django 4.2 on 2023-05-01 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='server_list_json',
            field=models.CharField(default="{'server-list': [1]}", max_length=300),
        ),
    ]
