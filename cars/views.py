from rest_framework import viewsets

from .models import (
    Brand,
    CarModel,
    CompleteSet,
    Car
)

from .serializers import (
    BrandSerializer,
    CarModelSerializer,
    CompleteSetSerializer,
    CarListSerializer,
    CarCreateSerializer
)


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer


class CompleteSetViewSet(viewsets.ModelViewSet):
    queryset = CompleteSet.objects.all()
    serializer_class = CompleteSetSerializer


class CarViewSet(viewsets.ModelViewSet):

    queryset = Car.objects.all()

    def get_serializer_class(self):

        if self.action in ["create", "update", "partial_update"]:
            return CarCreateSerializer

        return CarListSerializer