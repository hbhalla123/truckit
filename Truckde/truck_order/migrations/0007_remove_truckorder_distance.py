# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('truck_order', '0006_auto_20150628_0913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='truckorder',
            name='distance',
        ),
    ]
