from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from ..models.season import Season
from ..serializers.season import *

class SeasonViewSet(viewsets.ModelViewSet):
  """
  This viewset automatically provides `list`, `create`, `retrieve`,
  `update` and `destroy` actions.
  """
  queryset = Season.objects.all()
  serializer_class = SeasonSerializer