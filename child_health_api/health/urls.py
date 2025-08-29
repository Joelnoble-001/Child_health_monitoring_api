from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from health.views import ChildViewSet, HealthRecordViewSet, VaccinationViewSet

router = DefaultRouter()
router.register(r'children', ChildViewSet)
router.register(r'health-records', HealthRecordViewSet)
router.register(r'vaccinations', VaccinationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
