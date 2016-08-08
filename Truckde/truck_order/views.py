from django.core import serializers
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from truck_order.models import *
from django.core.mail import send_mail
import datetime

from django.forms import ModelForm
# Create your views here.

class OrderForm(ModelForm):
    class Meta:
        model = TruckOrder
        exclude = ['order_date', 'order_time']

def home(request):
	data=Vehicle.objects.all()
	print("how")
	form=OrderForm()

	return render(request,'base2.html',{"vehicle_list":data,'form':form})


		
def post_order(request):
    print(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save();
#            email_subject = 'Order confirmation'
 #           email_body = "Hey %s, thanks for using truckit. Our executive will call you soon." % (request.POST.get(customer_Name))

  #          send_mail(email_subject, email_body, 'rkap95@gmail.com',
   #             [email], fail_silently=False)
            return redirect('/thanku/')
    return redirect('home')

def thanks(request):
    now = datetime.datetime.now()
    ht = "<html><body>Thanks for placing your order at  %s.</body></html>" % now
    return render(request,'thanku.html')

		
def price_add(request):
	truckorder=get_object_or_404(TruckOrder,pk=request.POST.get('TruckOrder'))
	fare.order_fare=fare.money
	fare.save()
	return HttpResponse()
		
def vehicle_info(request):
	if request.method == 'GET':
		vehicles=Vehicle.objects.all()
		data=serializers.serialize("json",vehicles,indent=8)
		return HttpResponse(data,content_type='application/json')
#if request.method=='POST':
#		Truck_order.objects.create(customer_Name='customer_Name',source='source', Destination='Destination',phone_number='phone_number', Delivery_date='Delivery_date',Delivery_time='Delivery_time',vehicle_choice='vehicle_choice')
		
		#source=request.POST['source']
		#Destination=request.POST['Destination']
		#customer_Name=request.POST['customer_Name']
		#phone_number=request.POST['phone_number']
		#Delivery_date=request.POST['Delivery_date']
		#Delivery_time=request.POST['Delivery_time']
		#vehicle_choice=request.POST['vehicle_choice']
#def vehicles(request):
#	data=Vehicle.objects.all()
#	return render(request,'base.html',{"vehicle_list":data})

