from rest_framework import serializers
from .models import Drones, Medication


class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drones
        fields = ["serial_number", "model", "weight", "battery", "state", "medications"]
