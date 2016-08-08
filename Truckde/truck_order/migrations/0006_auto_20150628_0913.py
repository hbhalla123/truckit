# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('truck_order', '0005_auto_20150628_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truckorder',
            name='distance',
            field=models.IntegerField(default=0, max_length=20),
        ),
    ]
