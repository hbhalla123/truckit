from django.core import serializers
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from truck_order.models import *
import datetime
from django.forms import ModelForm
from django import forms
from django.forms.extras.widgets import SelectDateWidget


#class Truck_orderForm(ModelForm):
	#	class Meta:
	#		model = Truck_order
	#		fields = ['source', 'Destination', 'Delivery_date', 'Email','vehicle_choice']

# Creating a form to add an article.
	#form = Truck_orderForm()
	
#class SimpleForm(forms.Form):
 #   Pickup_date = forms.DateField(widget=SelectDateWidget)
	#Pickup_date.render()
                                   

from django.db import models 
from django import forms 
from datetimewidget.widgets 
import DateTimeWidget, DateWidget, TimeWidget 
# Bootstrap 3 
class testFormBootstrap3(forms.Form):
date = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3))
time = forms.TimeField(widget=TimeWidget(usel10n=True, bootstrap_version=3))


class yourForm(forms.ModelForm):
    class Meta:
        model = Truck_order
		fields = '__all__'
		exclude = ['source','Destination','Requirements','Order_date','Order_time','Email','vehicle_choice']
        widgets = {
            #Use localization and bootstrap 3
            'datetime': DateTimeWidget(attrs={'id':"Delivery_date"}, usel10n = True, bootstrap_version=3)
        }

