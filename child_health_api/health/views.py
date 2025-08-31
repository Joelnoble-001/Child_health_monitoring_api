from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Child, HealthRecord, Vaccination, Immunization, ClinicVisit, WeightRecord
from .serializers import ChildSerializer, HealthRecordSerializer, VaccinationSerializer, ImmunizationSerializer, ClinicVisitSerializer, WeightRecordSerializer

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

class ImmunizationViewSet(viewsets.ModelViewSet):
    queryset = Immunization.objects.all()
    serializer_class = ImmunizationSerializer
    permission_classes = [IsAuthenticated]

class ClinicVisitViewSet(viewsets.ModelViewSet):
    queryset = ClinicVisit.objects.all()
    serializer_class = ClinicVisitSerializer
    permission_classes = [IsAuthenticated]

class WeightRecordViewSet(viewsets.ModelViewSet):
    queryset = WeightRecord.objects.all()
    serializer_class = WeightRecordSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["get"])
    def malnourished(self, request):
        qs = self.get_queryset().filter(nutrition_status="Underweight")
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
