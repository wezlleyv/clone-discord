# Generated by Django 4.2 on 2023-05-07 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0002_alter_message_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='user_in_server',
            field=models.CharField(default={"{'users': []}"}, max_length=300),
        ),
    ]