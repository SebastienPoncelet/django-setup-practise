from rest_framework import serializers
from ..models.season import Season


class SeasonSerializer(serializers.ModelSerializer):
  """
  Serializer for all actions on Season model
  """
  
  country = serializers.StringRelatedField(many=True)

  class Meta:
    model = Season
    fields = [
      'id',
      'name',
      'code',
      'description',
      'country',
      'created_at',
      'updated_at'
    ]
    