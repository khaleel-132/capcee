from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import Template,loader
from .models import *

# Create your views here.



##super user created registered product model with admin panel

def add_product(request):
    prod=Product.objects.all()
    return render(request,'index.html',{'pro':prod})