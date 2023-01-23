from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from sales_service.models import customer,staff
from .forms import customerform
from .staff_views import staffDetails


# from .forms import customerform


def customerDetails(request):
       customers= customer.objects.all().values()
       
       
       return render(request,"crud customer/customercrud.html",{ 'customers':customers})
def customerCreation(request):
    return render(request,"crud customer/create_customer.html")


def createcustome(request):
    if request.method=="POST":
          CustomerName=request.POST["CustomerName"]
          CustomerPhoneNo=request.POST["CustomerPhoneNo"]
          
          CustomerAddress=request.POST["CustomerAddress"]
          Status=request.POST["Status"]
          Notes=request.POST["Notes"]
          CustomerEMail=request.POST[ "CustomerEMail"]
          
          createC=customer.objects.create(CustomerName=CustomerName,
                                          CustomerPhoneNo= CustomerPhoneNo,CustomerEMail=CustomerEMail,
                                          CustomerAddress=CustomerAddress,
                                          Status=Status,
                                          Notes=Notes)
          createC.save()
          return redirect(customerDetails)
      
# customer update

def updatecustomer(request, id):  

    customers = customer.objects.get(id=id)  
    form = customerform(request.POST, instance =customers)  
    if form.is_valid(): 
         
        form.save()  
        customers=customer.objects.all()
    else:
        form=customerform(instance=customers)
    return HttpResponseRedirect(reverse(customerDetails))

#delete customer
def deletecustomer(request, id):
  if request.method == 'POST':
    customers = customer.objects.get(id=id)
    customers.delete()
  return HttpResponseRedirect(reverse(customerDetails))
      
        
#customer view notes    
# def view_customer(request, id):
#   coustomers = customer.objects.get(id=id)
#   return HttpResponseRedirect(reverse(customerDetails))    

# landingpage view




def landing (request):
    return render(request,'landingpage.html')
# Userloginpage
def loginn(request):
    
    return render(request,'registration/login.html')
# signin
def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        User=authenticate(username=username,password=password)
        if User is not None:
            login(request,User)
           
            return redirect(staffDetails)
        else:
           return redirect(loginn) 

    
    
# dashboard
@login_required
def dashboard(request):
    return render(request,'index.html')
# userregisterpage
def userregister(request):
    return render(request,'registration/register.html')
# userregistration
def registeruser(request):
    if request.method=="POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        myuser=User.objects.create_user(username,email,password1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"your Account sucessfully created")
        
        return redirect(loginn)
def signout(request):
    logout(request)
    return redirect(landing)

# customer filter
    


    
    
    
    
    
    
    
    
    
    
    
    
    

# Create your views here.
