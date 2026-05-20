from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'password',
            'region',
        )

    def validate_phone(self, value):
        if not value.startswith('+996'):
            raise serializers.ValidationError("Номер должен начинаться с +996")
        return value

    def validate_email(self, value):
        return value.lower()

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            username=email,
            password=password
        )

        if not user:
            raise serializers.ValidationError("Неверный email или пароль")

        attrs['user'] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'region',
        )