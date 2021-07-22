from rest_framework import serializers
from ..models.colour import Colour


class ColourSerializer(serializers.ModelSerializer):
  """
  Serializer for all actions on Colour model
  """

  class Meta:
    model = Colour
    fields = [
      'name',
      'rgb_code',
      'description',
      'created_at',
      'updated_at'
    ]
    