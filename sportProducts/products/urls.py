from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .views import *

router = routers.DefaultRouter()
router.register(r'colours', ColourViewSet)

urlpatterns = [
    path(r'', include(router.urls))
]