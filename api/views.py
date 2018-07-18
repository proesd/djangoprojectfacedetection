from django.shortcuts import render
from rest_framework import generics,viewsets
from .serializers import BukuTamuSeliazers
from .models import BukuTamu

class BukuTamuViews(viewsets.ModelViewSet):
    """This class defines the create behavior of our rest api."""
    queryset = BukuTamu.objects.all()
    serializer_class = BukuTamuSeliazers
    
# Create your views here.
