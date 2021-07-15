from django.db import models

# TODO: Check if it's necessary to add updated_at and created_at fields
class Cycle(models.Model):
    active_duration = models.IntegerField()
    inactive_duration = models.IntegerField()
    number_repetition = models.IntegerField()
    # pub_date = models.DateTimeField('date published')
