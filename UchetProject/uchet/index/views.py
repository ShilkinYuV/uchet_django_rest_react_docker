from django.shortcuts import render, get_object_or_404

from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.settings import api_settings

from .permissions import UchetPermissions

from .serializers import DepartmentsSerializer, CheludiSerializer, TechnicsSerializer, UserPorfileSerializer
from .models import Cheludi, Departments, Technics, UserProfile


class DepartmentsViewSet(viewsets.ModelViewSet):
    """ViewSet для управления списком отделов"""
    queryset = Departments.objects.all() # список всех объектов
    serializer_class = DepartmentsSerializer # класс сериализатора
    permission_classes = (UchetPermissions,) # классы разрешений 
    authentication_classes = (TokenAuthentication,) # класс авторизации


class CheludisViewSet(viewsets.ModelViewSet):
    """ViewSet для управления списком челюдей"""
    queryset = Cheludi.objects.all()
    serializer_class = CheludiSerializer
    permission_classes = (UchetPermissions,)
    authentication_classes = (TokenAuthentication,)


class TechnicsViewSet(viewsets.ModelViewSet):
    """ViewSet для управления списком техники"""
    queryset = Technics.objects.all()
    serializer_class = TechnicsSerializer
    permission_classes = (UchetPermissions,)
    authentication_classes = (TokenAuthentication,)


class UserLoginApiView(ObtainAuthToken):
    """Создание токена авторизации"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileViewSet(viewsets.ModelViewSet):
    """Viewset для создания профилей"""
    serializer_class = UserPorfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    search_fields = ('name', 'email',)
    permission_classes = (
        UchetPermissions,
    )
