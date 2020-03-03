from django.shortcuts import render
from .serializers import MySerializer
from rest_framework import viewsets
from .models import List

class Crud(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class=MySerializer



# Create your views here.
