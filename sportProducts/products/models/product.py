from django.db import models
from .colour import *
from .sport import *
from .category import *
from .brand import *
from .size import *
from .availability import *

class Product(models.Model):
    colour = models.ForeignKey(Colour, on_delete=models.CASCADE, related_name='product')
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name='product')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='product')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='product')
    availability = models.ForeignKey(Availability, on_delete=models.CASCADE, related_name='product')
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=200)
    variant = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "{} {}".format(self.name, self.sku)
