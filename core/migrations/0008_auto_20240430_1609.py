# Generated by Django 2.1.7 on 2024-04-30 19:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20240430_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 4, 30, 16, 9, 6, 447328)),
        ),
    ]
