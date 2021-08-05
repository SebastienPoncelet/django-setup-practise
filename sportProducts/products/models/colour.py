from django.db import models


class Colour(models.Model):
  name = models.CharField(max_length=200)
  rgb_code = models.CharField(max_length=200)
  description = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return "{} {}".format(self.name, self.description)
