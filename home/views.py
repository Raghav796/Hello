from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
import pdb

# Create your views here.
def index (request):
    # return HttpResponse("this is home page")
    return render(request,'index.html')

def about (request):
   #  return HttpResponse("this is about page")
   return render(request,'about.html')

def scoops (request):
   #  return HttpResponse("this is about page")
   return render(request,'scoops.html')

def cones (request):
   #  return HttpResponse("this is about page")
   return render(request,'cones.html')

def tubs (request):
   #  return HttpResponse("this is about page")
   return render(request,'tubs.html')

def services (request):
   #  return HttpResponse("this is services page")
   return render(request,'services.html')
   # return render(request,'scoops.html')
   # return render(request,'tubs.html')


def treatBars(request):
   return render(request,'bars.html')

def contact (request):
   if request.method == "POST":
      pdb.set_trace()
      name = request.POST.get('name')
      email = request.POST.get('email')
      phone = request.POST.get('phone')
      message = request.POST.get('message')  
      contact = Contact(name=name,email=email,phone=phone,message=message,date=datetime.today())
      contact.save()
      messages.success(request, 'Your Form has been submitted!')
      
   # return render(request,'contact.html')
   return render(request,'contact.html')
    

