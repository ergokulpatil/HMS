from django.contrib import admin
from django.urls import path,include
from . views import *

urlpatterns = [

    path('patient-profile-list/',PatientProfileListView.as_view(),name='patient-profile-list'),
]
