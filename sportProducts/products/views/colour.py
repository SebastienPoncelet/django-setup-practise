from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from ..models.colour import Colour
from ..serializers.colour import *

class ColourViewSet(viewsets.ModelViewSet):
  """
  This viewset automatically provides `list`, `create`, `retrieve`,
  `update` and `destroy` actions.
  """
  queryset = Colour.objects.all()
  serializer_class = ColourSerializer