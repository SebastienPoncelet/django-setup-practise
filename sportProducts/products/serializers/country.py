from rest_framework import serializers
from ..models.country import Country


class CountrySerializer(serializers.ModelSerializer):
  """
  Serializer for all actions on Country model
  """

  class Meta:
    model = Country
    fields = [
      'id',
      'name',
      'code',
      'region',
      'created_at',
      'updated_at'
    ]
    