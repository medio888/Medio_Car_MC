from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="models")
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.brand} {self.name}"


class CompleteSet(models.Model):
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name="sets")
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.model} {self.name}"


class Car(models.Model):

    COLOR_CHOICES = [
        ("black", "Черный"),
        ("white", "Белый"),
        ("gray", "Серый"),
        ("red", "Красный"),
        ("green", "Зеленый"),
    ]

    FUEL_CHOICES = [
        ("petrol", "Бензин"),
        ("diesel", "Дизель"),
        ("hybrid", "Гибрид"),
        ("electric", "Электро"),
    ]

    DRIVE_CHOICES = [
        ("fwd", "Передний"),
        ("rwd", "Задний"),
        ("awd", "Полный"),
    ]

    TRANSMISSION_CHOICES = [
        ("auto", "Автомат"),
        ("manual", "Механика"),
        ("cvt", "Вариатор"),
    ]

    BODY_CHOICES = [
        ("sedan", "Седан"),
        ("suv", "Внедорожник"),
        ("coupe", "Купе"),
        ("wagon", "Универсал"),
        ("hatchback", "Хэтчбек"),
    ]

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    complete_set = models.ForeignKey(CompleteSet, on_delete=models.CASCADE)

    year = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)

    color = models.CharField(max_length=20, choices=COLOR_CHOICES)
    body_type = models.CharField(max_length=20, choices=BODY_CHOICES)

    volume = models.DecimalField(max_digits=4, decimal_places=1)

    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES)
    drive_type = models.CharField(max_length=20, choices=DRIVE_CHOICES)
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES)

    def __str__(self):
        return f"{self.brand} {self.model}"