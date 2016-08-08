# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('truck_order', '0003_truckorder_order_fare'),
    ]

    operations = [
        migrations.AddField(
            model_name='truckorder',
            name='distance',
            field=models.CharField(max_length=255, default=30),
            preserve_default=False,
        ),
    ]
