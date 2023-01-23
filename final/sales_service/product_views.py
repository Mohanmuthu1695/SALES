import json
from django.shortcuts import render,redirect
from sales_service.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets,filters
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend


#productview 
def productview(request):
    if request.method == 'GET':
   
        products=product.objects.all().values()
        return render(request,"crud product/product_crud.html",{ 'products':products})
def productsave(request):
    if request.method=="POST":
       
       P_ID=request.POST["P_ID"]
       Name=request.POST["Name"]
       category=request.POST["category"]
       M_R_P=request.POST["M_R_P"]
       Rate=request.POST["Rate"]
       Quantity=request.POST["Quantity"]
       Units=request.POST["Units"]
       Status=request.POST["Status"]
       Notes=request.POST["Notes"]
       if len(request.FILES) !=0:
        product_image=request.FILES["product_image"]
        products=product.objects.create(P_ID=P_ID,Name=Name,category=category,M_R_P=M_R_P,Rate=Rate,
                                           Quantity=Quantity,Units=Units,Status=Status,Notes=Notes,product_image=product_image )
        products.save()
       return redirect(productview)
# product update

def updateproduct(request, id):  

    products = product.objects.get(id=id)  
    form = productform(request.POST, instance =products)  
    if form.is_valid(): 
         
        form.save()  
        products=product.objects.all()
    else:
    
        form=productform(instance=products)
    return HttpResponseRedirect(reverse(productview))

#delete product
def deleteproduct(request, id):
  if request.method == 'POST':
    products = product.objects.get(id=id)
    products.delete()
  return HttpResponseRedirect(reverse(productview))

        


def createproduct(request):
    return render (request,"crud product/create_product.html")
#product dashboard
def Pdashboard(request):
    products=product.objects.all().values()
    products_count=products.count()
    return render(request,"dashboard/product_dashboard.html",{ 'products':products,'products_count':products_count})
    
    
#  #sales page

def demo(request):
    return render(request,"demo.html")
def invoicepage(request):
    dropdown1=customer.objects.all()
    dropdown2=product.objects.all()
    # CName=request.POST.get('CustomerName')
    # cdata=customer.objects.raw('Select * FROM sales_service_customer WHERE CustomerName="'+CName+'"')
    return render(request,"crud product/sales.html",{'dropdown1':dropdown1,'dropdown2':dropdown2,})  


class productviewset(viewsets.ModelViewSet):
    serializer_class = productSerializer
    queryset = product.objects.all()
    filter_backends=[ DjangoFilterBackend,filters.SearchFilter ]
    filterset_fields=["Name","M_R_P","Rate"]
    search_fields=["Name"]
