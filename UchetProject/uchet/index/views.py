from django.shortcuts import render,get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.settings import api_settings

from .serializers import DepartmentsSerializer, CheludiSerializer,TechnicsSerializer,UserPorfileSerializer
from .models import Cheludi, Departments, Technics, UserProfile

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

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = UserPorfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    search_fields = ('name', 'email',)