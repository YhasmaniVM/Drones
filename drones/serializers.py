from rest_framework import serializers
from .models import Drones, Medication


class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drones
        fields = ["id", "serial_number", "model", "weight", "battery", "state", "medications"]


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ["id", "name", "weight", "code", "image"]
