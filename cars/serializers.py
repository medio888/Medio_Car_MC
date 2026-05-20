from rest_framework import serializers

from .models import (
    Brand,
    CarModel,
    CompleteSet,
    Car
)


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = "__all__"


class CarModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarModel
        fields = "__all__"


class CompleteSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompleteSet
        fields = "__all__"


class CarListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = "__all__"


class CarCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = "__all__"