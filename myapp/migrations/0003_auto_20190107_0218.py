# Generated by Django 2.1.4 on 2019-01-07 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_car_event'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]