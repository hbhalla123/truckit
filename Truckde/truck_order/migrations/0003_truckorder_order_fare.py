# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('truck_order', '0002_remove_truckorder_order_fare'),
    ]

    operations = [
        migrations.AddField(
            model_name='truckorder',
            name='order_fare',
            field=models.IntegerField(default=0, max_length=10),
            preserve_default=True,
        ),
    ]
