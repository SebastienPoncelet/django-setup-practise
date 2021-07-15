from django.db import models


class Cycle(models.Model):
    active_duration = models.IntegerField()
    inactive_duration = models.IntegerField()
    number_repetition = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
