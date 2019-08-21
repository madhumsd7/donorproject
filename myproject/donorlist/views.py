from django.shortcuts import render,redirect
from .models import donorlist
from django.contrib import messages

# Create your views here.
def home(request):  
    return render(request,'base.html',)

def register(request): 

    if request.method == 'POST':
       name = request.POST["name"]
       email = request.POST["email"]
       blood = request.POST["blood"]
       mobile_number = request.POST["mobile_number"]
       place = request.POST["place"]
    
       if donorlist.objects.filter(mobile_number=mobile_number).exists():
          messages.info(request,'mobile number exists')
          return redirect('/register')
       elif donorlist.objects.filter(email=email).exists():
          messages.info(request,'email taken')
          return redirect('/register') 
       else:
          b = donorlist(name=name, blood=blood, email=email, mobile_number=mobile_number, place=place)
          b.save()
          return render(request,'msg.html',)
    else:
      return render(request,'register.html',)

def view(request):    
    return render(request,'view.html',) 
   
def about(request):  
    return render(request,'about.html',)

def a(request): 
    a= donorlist.objects.filter(blood__contains='A+')
    return render(request,'a.html',{'a':a}) 
    
def b(request):
    b = donorlist.objects.filter(blood__contains='B+')
    return render(request,'b.html',{'b':b})  

def contact(request):  
    return render(request,'contact.html',)


