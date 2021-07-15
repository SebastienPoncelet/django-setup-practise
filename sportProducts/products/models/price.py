from django.db import models
from .product import *

# TODO: Check if it's necessary to add updated_at and created_at fields
class Country(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    currency = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    
