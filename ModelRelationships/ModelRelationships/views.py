from django.urls import path 
from .models import Customer, Order
from django.shortcuts import render
from django.http import HttpResponse

#def customerpage(request):
 #   customer = Customer.objects.all()
  #  order = Order.objects.all()
   # #context = {
     #   'form':form
    #}
    #return render(request, 'customerpage.html')