from django.shortcuts import render
from rest_framework import viewsets
from .models import Child, HealthRecord, Vaccination
from .serializers import ChildSerializer, HealthRecordSerializer, VaccinationSerializer

# Create your views here.
class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

class HealthRecordViewSet(viewsets.ModelViewSet):
    queryset = HealthRecord.objects.all()
    serializer_class = HealthRecordSerializer

class VaccinationViewSet(viewsets.ModelViewSet):
    queryset = Vaccination.objects.all()
    serializer_class = VaccinationSerializer
