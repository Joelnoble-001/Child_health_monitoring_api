from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    HealthRecordViewSet, VaccinationViewSet,
    ImmunizationViewSet, ClinicVisitViewSet, WeightRecordViewSet
)

router = DefaultRouter()
router.register(r"health-records", HealthRecordViewSet)
router.register(r"vaccinations", VaccinationViewSet)
router.register(r"immunizations", ImmunizationViewSet, basename="immunizations")
router.register(r"visits", ClinicVisitViewSet, basename="visits")
router.register(r"growth", WeightRecordViewSet, basename="growth")

urlpatterns = [
    path("", include(router.urls)),
    # Custom endpoint for malnourished stats
    path("stats/malnourished/", WeightRecordViewSet.as_view({"get": "malnourished"})),
]


