from django.shortcuts import render
from rest_framework import viewsets
from .models import Type
from .serializers import TypeSerializer

class TypeViewset(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    