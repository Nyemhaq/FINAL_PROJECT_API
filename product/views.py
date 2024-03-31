from django.shortcuts import render
from rest_framework import viewsets
from .models import Product,Review
from .serializers import ProductSerializer,ReviewSerializer

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer