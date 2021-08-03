from django.db import models
from .season import *


class Country(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='country')
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "{}".format(self.name)
