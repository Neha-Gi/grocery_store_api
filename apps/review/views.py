from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Review
from .serializer import ReviewSerializer
# Create your views here.


@api_view(["GET"])
def review_list(request):
    data=Review.objects.all()
    
    review = ReviewSerializer(data, many=True)
    return Response(review.data)
