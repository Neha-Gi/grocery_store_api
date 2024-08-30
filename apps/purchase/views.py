#from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from apps.purchase.models import Cart
from apps.purchase.serializer import CartSerializer

"""curl http://127.0.0.1:8000/api/v1/cart/
curl -u admin:admin http://127.0.0.1:8000/api/v1/cart/git@github.com:Neha-Gi/grocery_store_api.git 
"""
#Function-base view
@api_view(['GET']) # by default , it uses a 'GET' method
@permission_classes([IsAuthenticated])
def view_cart(request):
    # Get all items using ORM
    cart = Cart.objects.all()

    # Deserialize using the CartSerializer
    data = CartSerializer(cart,many=True)

    return Response(data.data, status=status.HTTP_200_OK)

#@api_view(['POST'])
#def create_cart_item(request):
 #   serializer = CartSerializer