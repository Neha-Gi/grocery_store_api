from django.urls import path
from . import views

app_name = 'purchase-urls'
urlpatterns = [
    path("cart/",views.view_cart,name='view_items'),
    
   
]
