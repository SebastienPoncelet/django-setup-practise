from django.db import models


class Size(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
