from rest_framework import serializers
from .models import Child, HealthRecord, Vaccination, Immunization, ClinicVisit, WeightRecord

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = "__all__"

class HealthRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthRecord
        fields = "__all__"

class VaccinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccination
        fields = "__all__"

class ImmunizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Immunization
        fields = "__all__"

class ClinicVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicVisit
        fields = "__all__"

class WeightRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightRecord
        fields = "__all__"
