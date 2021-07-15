from django.db import models

# TODO: Check if it's necessary to add updated_at and created_at fields
class Category(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
