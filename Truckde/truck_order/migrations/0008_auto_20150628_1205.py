# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('truck_order', '0007_remove_truckorder_distance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truckorder',
            name='order_fare',
            field=models.IntegerField(default=0),
        ),
    ]
