from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from rest_framework.generics import get_object_or_404


class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.PositiveIntegerField()
    is_active = models.BooleanField(null=True, blank=True, default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return f'{self.id}: {self.name}'


class Category(models.Model):
    name = models.CharField(max_length=32)