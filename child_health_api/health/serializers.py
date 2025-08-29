from rest_framework import serializers
from .models import Child, HealthRecord, Vaccination

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
