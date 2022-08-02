from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from . models import *
from .Serializers import *
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_bulk import (ListBulkCreateUpdateDestroyAPIView)
# Create your views here.


def home(request):
    return HttpResponse( "Welcome to HMS")


class PatientProfileListView(generics.ListCreateAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileserializer