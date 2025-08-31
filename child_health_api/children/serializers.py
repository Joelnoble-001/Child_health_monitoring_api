from rest_framework import serializers
from .models import Child, Caregiver

class CaregiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caregiver
        fields = "__all__"

class ChildSerializer(serializers.ModelSerializer):
    caregiver = CaregiverSerializer(read_only=True)
    caregiver_id = serializers.PrimaryKeyRelatedField(
        queryset=Caregiver.objects.all(), source="caregiver", write_only=True
    )

    class Meta:
        model = Child
        fields = ["id", "first_name", "last_name", "dob", "gender",
                  "caregiver", "caregiver_id", "address", "community"]
