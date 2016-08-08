from django.db import models
from django.core.validators import RegexValidator


class Vehicle(models.Model):
	vehicle_name = models.CharField(max_length=255)
	vehicle_price=models.IntegerField(default = 0)
  
	def __str__(self):             
		return self.vehicle_name


class TruckOrder(models.Model):
	customer_Name = models.CharField(max_length=255)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(max_length=15,validators=[phone_regex], blank=True) # validators should be a list
	source = models.CharField(max_length=255)
	destination = models.CharField(max_length=255)
	customer_Email=models.EmailField(max_length=255)
	order_fare=models.CharField(max_length=10,default=0)
	order_date = models.DateField(auto_now_add = True)
	order_time = models.TimeField(auto_now_add=True)
	delivery_date=models.DateField()
	delivery_time=models.TimeField()
	vehicle_choice = models.ForeignKey(Vehicle)
	def __str__(self):             
		return self.source
