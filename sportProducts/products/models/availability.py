from django.db import models
from .season import *
from .cycle import *

# TODO: Check if it's necessary to add updated_at and created_at fields
class Country(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE)
    is_active = models.BooleanField()
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
