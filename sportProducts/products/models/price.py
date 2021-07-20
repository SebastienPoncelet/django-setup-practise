from django.db import models
from .product import *


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='price')
    amount = models.IntegerField()
    currency = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
