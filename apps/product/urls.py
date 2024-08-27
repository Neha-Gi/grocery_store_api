from django.urls import path
from . import views

app_name = 'product-url'
urlpatterns = [
    path("list/", views.product_list, name="list-product"),
    path("create/", views.create_product, name="create-product"),
]
