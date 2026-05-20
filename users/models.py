from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email обязателен")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None

    REGIONS = (
        ('bishkek', 'Bishkek'),
        ('osh', 'Osh'),
        ('chuy', 'Chuy'),
        ('jalal_abad', 'Jalal-Abad'),
        ('issyk_kul', 'Issyk-Kul'),
        ('naryn', 'Naryn'),
        ('talas', 'Talas'),
        ('batken', 'Batken'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    phone = models.CharField(max_length=13, unique=True)
    email = models.EmailField(unique=True)

    region = models.CharField(max_length=50, choices=REGIONS)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email