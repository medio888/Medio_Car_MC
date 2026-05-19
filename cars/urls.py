from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    BrandViewSet,
    CarModelViewSet,
    CompleteSetViewSet,
    CarViewSet
)

router = DefaultRouter()

router.register(r"brands", BrandViewSet)
router.register(r"models", CarModelViewSet)
router.register(r"complete-sets", CompleteSetViewSet)
router.register(r"cars", CarViewSet)

urlpatterns = [
    path("", include(router.urls)),
]