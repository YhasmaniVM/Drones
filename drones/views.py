from django.http import JsonResponse
from .models import Drones, Medication
from .serializers import DroneSerializer, MedicationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def drones_list(request, format=None):
    if request.method == 'GET':
        drones = Drones.objects.all()
        serializer = DroneSerializer(drones, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DroneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def drones_detail(request, id, format=None):
    try:
        drones = Drones.objects.get(pk=id)
    except Drones.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DroneSerializer(drones)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DroneSerializer(drones, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drones.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def drones_medication_detail(request, id, format=None):
    try:
        drones = Drones.objects.get(pk=id)
    except Drones.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        if drones.medications.all():
            serializer = MedicationSerializer(drones.medications.all(), many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def drones_available(request, format=None):
    if request.method == 'GET':
        drones = Drones.objects.filter(state='idle')
        if drones.exists():
            serializer = DroneSerializer(drones, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def drones_battery_detail(request, id, format=None):
    try:
        drones = Drones.objects.get(pk=id)
    except Drones.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DroneSerializer(drones)
        return Response({'battery': serializer.data.get('battery')})
