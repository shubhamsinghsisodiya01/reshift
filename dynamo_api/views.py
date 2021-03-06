from django.shortcuts import render
from django.http import HttpResponse
from .models import SensorPi
from .serializers import SensorPiSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework import status as http_status
import json
# Create your views here.
def home(request):
    print("Hello ")
    read_data()
    return HttpResponse("success")

def read_data():
    power_data =  SensorPi.scan()

class SensorPiViewSet(viewsets.ViewSet):
    
    def list(self, request):
        queryset = SensorPi.scan()
        serializer = SensorPiSerializer(queryset, many=True)
        # data = json.dumps(serializer.data)
        data = serializer.data
        response = Response(data)
        response['Access-Control-Allow-Origin'] = "*"
        return response
    def retrieve(self, request, pk=None):
        queryset = SensorPi.scan()
        user = get_object_or_404(queryset, pk=pk)
        serializer = SensorPiSerializer(user)
        return Response(serializer.data)