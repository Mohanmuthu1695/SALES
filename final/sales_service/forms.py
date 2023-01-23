from .models import *
from django.forms import ModelForm

class customerform(ModelForm):
   
    class Meta:
        model=customer
        fields=['CustomerName','CustomerPhoneNo','CustomerEMail','CustomerAddress','Status','Notes']
class staffform(ModelForm):
    class Meta:
        model=staff
        fields=['EMP_ID','EMP_Name','Email','D_O_B','Qualifiaction','Address','Role','Mobile','Join_date','Status','Notess']
class productform(ModelForm):
    class Meta:
        model=product
        fields=['P_ID','Name','category','M_R_P','Rate','Quantity','Units','product_image','Status','Notes']