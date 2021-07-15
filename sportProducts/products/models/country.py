from django.db import models
from .season import *

# TODO: Check if it's necessary to add updated_at and created_at fields
class Country(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
