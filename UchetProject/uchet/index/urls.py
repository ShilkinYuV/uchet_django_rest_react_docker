from index import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'departments', views.DepartmentsViewSet,
                basename='departments')
router.register(r'cheludis', views.CheludisViewSet, basename='cheludis')
router.register(r'profile',views.UserProfileViewSet,basename='profile')
router.register(r'technics', views.TechnicsViewSet, basename='technics')

urlpatterns = [
    path('login/',views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
