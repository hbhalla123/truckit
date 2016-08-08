# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TruckOrder',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('customer_Name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15, blank=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('source', models.CharField(max_length=255)),
                ('order_fare', models.IntegerField(max_length=10)),
                ('destination', models.CharField(max_length=255)),
                ('order_date', models.DateField(auto_now_add=True)),
                ('order_time', models.TimeField(auto_now_add=True)),
                ('delivery_date', models.DateField()),
                ('delivery_time', models.TimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('vehicle_name', models.CharField(max_length=255)),
                ('vehicle_price', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='truckorder',
            name='vehicle_choice',
            field=models.ForeignKey(to='truck_order.Vehicle'),
            preserve_default=True,
        ),
    ]
