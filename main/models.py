from django.db import models


class Category(models.Model):
    name = models.CharField("категория", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField("подкатегория", max_length=100)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='subcategories'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "подкатегория"
        verbose_name_plural = "подкатегории"

    def __str__(self):
        return self.name