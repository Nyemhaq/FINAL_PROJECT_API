from django.shortcuts import render
from rest_framework import viewsets
from .models import Size
from .serializers import SizeSerializer

class SizeViewset(viewsets.ModelViewSet):
    queryset =  Size.objects.all()
    serializer_class = SizeSerializer
    