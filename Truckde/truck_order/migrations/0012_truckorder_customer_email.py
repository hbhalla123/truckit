# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-07 13:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('truck_order', '0011_auto_20150702_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='truckorder',
            name='customer_Email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
