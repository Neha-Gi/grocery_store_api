#from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.purchase.models import Cart
from apps.purchase.serializer import CartSerializer

#Function-base view
@api_view(['GET']) # by default , it uses a 'GET' method
def view_cart(request):
    # Get all items using ORM
    cart = Cart.objects.all()

    # Deserialize using the CartSerializer
    data = CartSerializer(cart,many=True)

    return Response(data.data, status=status.HTTP_200_OK)