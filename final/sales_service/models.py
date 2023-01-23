from django.db import models

class customer(models.Model):
    CustomerName=models.CharField( max_length=50)
    CustomerPhoneNo=models.IntegerField()
    CustomerEMail=models.EmailField(max_length=254)
    CustomerAddress=models.CharField(max_length=450)
    Status=models.CharField(max_length=50,default="active")
    Notes=models.TextField(max_length=1000, default=" " )
  
    
class staff(models.Model):
    EMP_ID=models.IntegerField()
    EMP_Name=models.CharField( max_length=254)
    Email=models.EmailField( max_length=254)
    D_O_B=models.DateField(auto_now=False)
    Qualifiaction=models.CharField( max_length=50)
    Address=models.CharField(max_length=350)
    Role=models.CharField(max_length=50)
    Mobile=models.IntegerField()
    Join_date=models.DateField( auto_now=False)
    Status=models.CharField( max_length=50)
    Notess=models.TextField( )
    
class product(models.Model):
    P_ID=models.IntegerField()
    Name=models.CharField( max_length=50)
    category=models.CharField( max_length=50)
    M_R_P=models.IntegerField()
    Rate=models.IntegerField()
    Quantity=models.IntegerField()
    Units=models.IntegerField()
    product_image=models.ImageField(upload_to="media/")
    Status=models.CharField(max_length=50)
    Notes=models.CharField(max_length=50)    
    
    
    

# Create your models here.
