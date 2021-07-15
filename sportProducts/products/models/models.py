from django.db import models


class Colour(models.Model):
    name = models.CharField(max_length=200)
    rgb_code = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')


class Product(models.Model):
    question = models.ForeignKey(Colour, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=200)
    variant = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0)