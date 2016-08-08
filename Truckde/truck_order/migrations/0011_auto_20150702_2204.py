# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('truck_order', '0010_auto_20150629_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truckorder',
            name='order_fare',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
