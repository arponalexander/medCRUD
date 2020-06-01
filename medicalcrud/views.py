from django.shortcuts import render
from rest_framework import viewsets
from .models import Medication_B00, Medication_R01, Medication_R02
from .serializers import Medication_B00_Serializer, Medication_R01_Serializer, Medication_R02_Serializer
import coreapi
from rest_framework.schemas import AutoSchema


class MedicationR01View(viewsets.ModelViewSet):
    queryset = Medication_R01.objects.all()
    serializer_class = Medication_R01_Serializer


class MedicationR02View(viewsets.ModelViewSet):
    queryset = Medication_R02.objects.all()
    serializer_class = Medication_R02_Serializer


class MedicationB00View(viewsets.ModelViewSet):
    queryset = Medication_B00.objects.all()
    serializer_class = Medication_B00_Serializer
