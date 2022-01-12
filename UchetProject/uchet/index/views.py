from django.shortcuts import render,get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import DepartmentsSerializer, CheludiSerializer,TechnicsSerializer
from .models import Cheludi, Departments, Technics

class DepartmentsViewSet(viewsets.ModelViewSet):
    """ViewSet для управления списком отделов"""
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer

class CheludisViewSet(viewsets.ModelViewSet):
    """ViewSet для управления списком челюдей"""
    queryset = Cheludi.objects.all()
    serializer_class = CheludiSerializer


class TechnicsViewSet(viewsets.ModelViewSet):
    """ViewSet для управления списком техники"""
    queryset = Technics.objects.all()
    serializer_class = TechnicsSerializer
