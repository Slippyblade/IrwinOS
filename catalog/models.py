# models.py
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

class BaseItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class StockItem(BaseItem):
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name