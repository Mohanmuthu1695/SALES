# from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from sales_service import views
from django.contrib.auth import views as auth_views
from sales_service import staff_views
from sales_service import product_views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # path("",views.landing,name='landingpage'),
    
    
    path("",views.loginn,name="login"),
    path('signin/',views.signin,name='signin'),
    path("customerdetail/",views.customerDetails,name="customerdetail"),
    path("register/",views.userregister,name="register"),
    path("createuser/",views.registeruser,name="registeruser"),
    path('signout/',views.signout,name="signout"),
    path("createpath/",views.customerCreation,name="createpath"),
    path("createcustomer/",views.createcustome,name="create"),
    # path('<int:id>', views.view_customer, name='view_customer'),
    path("updatecustomer/<int:id>",views.updatecustomer,name='updatecustomer'),
    path('deletecustomer/<int:id>/', views.deletecustomer, name='deletecustomer'),
    
    
    
    
    
    
    
    
    # staffs url
    # path("staffviews/",staff_views.staffDetails,name="staffviews"),
    path("createstaff/",staff_views.staffcreation,name="staffcreation"),
    path("staffform/",staff_views.staffview,name="staffview"),
    path("staffdisplay/",staff_views.staffDetails,name="staffdetails"),
    path("updatestaff/<int:id>",staff_views.updatestaff,name='updatestaff'),
    path('deletestaff/<int:id>/', staff_views.deletestaff, name='deletestaff'),
    path("staffdata/",staff_views.staffview2,name="staffdata"),
    
    
    #product urls...
    path("createproduct/",product_views.createproduct,name="createproduct"),
    path("viewproduct",product_views.productview,name="productview"),
    path("saveproduct/",product_views.productsave,name="productsave"),
    path("updateproduct/<int:id>",product_views.updateproduct,name='updateproduct'),
    path('deleteproduct/<int:id>/', product_views.deleteproduct, name='deleteproduct'),
    
    
    
    
    #product dashboard
    path("ProductDashboard/",product_views.Pdashboard,name='Pdashboard'),
    path("demo/",product_views.demo,name="demo"),
    
    
    
    
    
    
    #sales
    path("invoice/",product_views.invoicepage,name="invoicepage"),
    
    
    
    
  
  
]


router=DefaultRouter()
router.register("api/product",product_views.productviewset,basename="product")
urlpatterns += router.urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)