from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChildViewSet, CaregiverViewSet

router = DefaultRouter()
router.register(r"children", ChildViewSet, basename="children")
router.register(r"caregivers", CaregiverViewSet, basename="caregivers")

urlpatterns = [
    path("", include(router.urls)),
    
]
