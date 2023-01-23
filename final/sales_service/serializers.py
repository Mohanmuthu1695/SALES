from rest_framework import serializers
from .models import *
class productSerializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields=('P_ID','Name','category','M_R_P','Rate','Quantity','Units','product_image','Status','Notes')