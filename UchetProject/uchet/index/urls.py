from .views import CheludisViewSet, DepartmentsViewSet, TechnicsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'departments', DepartmentsViewSet, basename='departments')
router.register(r'cheludis', CheludisViewSet, basename='cheludis')
router.register(r'technics', TechnicsViewSet, basename='technics')

urlpatterns = router.urls