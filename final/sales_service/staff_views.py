from django.shortcuts import render,redirect
from sales_service.models import staff
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *
from .views import *
from .product_views import *
from .models import *
#staffview 2
def staffview2(request):
    staffs=staff.objects.all().values()
    return render(request,"crud staff/viewstaff2.html",{ 'staffs':staffs})

 #staff views
def staffDetails(request):
        staffs= staff.objects.all().values()
        customers= customer.objects.all().values()
        customers_count=customers.count()
        staffs_count=staffs.count()
        products=product.objects.all().values()
        products_count=products.count()
        return render(request,"dashboard/maindashboard.html",{ 'staffs':staffs,"staffs_count":staffs_count,
                                                              "customers":customers,"customers_count":customers_count,
                                                              "products":products,"products_count":products_count})
# create staff

def staffcreation(request):
    if request.method=="POST":
        EMP_ID=request.POST["EMP_ID"]
        EMP_Name=request.POST["EMP_Name"]
        Email=request.POST["Email"]
        D_O_B=request.POST['D_O_B']
        Qualifiaction=request.POST["Qualifiaction"]
        Address=request.POST["Address"]
        Role=request.POST["Role"]
        Mobile=request.POST["Mobile"]
        Join_date=request.POST["Join_date"]
        Status=request.POST['Status']
        Notess=request.POST["Notess"]
        creates=staff.objects.create(EMP_ID=EMP_ID,EMP_Name=EMP_Name,Email=Email,D_O_B=D_O_B,
                                     Qualifiaction=Qualifiaction,Address=Address,Role=Role,
                                     Mobile=Mobile,Join_date=Join_date,Status=Status,Notess=Notess
                                     )
        creates.save()
        return redirect(staffDetails)
  #createpage      
def staffview(request):
    return render (request,"crud staff/create_staff.html")   
# staff update

def updatestaff(request, id):  

    staffs = staff.objects.get(id=id)  
    form = staffform(request.POST, instance =staffs)  
    if form.is_valid(): 
         
        form.save()  
        staffs=staff.objects.all()
    else:
        form=staffform(instance=staffs)
    return HttpResponseRedirect(reverse(staffview2))

#delete staff
def deletestaff(request, id):
  if request.method == 'POST':
    staffs = staff.objects.get(id=id)
    staffs.delete()
  return HttpResponseRedirect(reverse(staffview2))
      
     