from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from ..models.country import Country
from ..serializers.country import *

class CountryViewSet(viewsets.ModelViewSet):
  """
  This viewset automatically provides `list`, `create`, `retrieve`,
  `update` and `destroy` actions.
  """
  queryset = Country.objects.all()
  serializer_class = CountrySerializer