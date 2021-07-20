from django.db import models
from .season import *
from .cycle import *

class Availability(models.Model):
    season = models.OneToOneField(Season, null=True, on_delete=models.CASCADE, related_name='availability')
    cycle = models.OneToOneField(Cycle, null=True, on_delete=models.CASCADE, related_name='availability')
    is_active = models.BooleanField()
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
