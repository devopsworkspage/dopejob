# Generated by Django 2.0.2 on 2018-07-29 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0014_booking_car'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='user',
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]
