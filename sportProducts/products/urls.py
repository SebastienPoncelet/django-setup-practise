from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .views import *

router = routers.DefaultRouter()
router.register(r'colours', ColourViewSet)
router.register(r'seasons', SeasonViewSet)
router.register(r'countries', CountryViewSet)

urlpatterns = [
    path(r'', include(router.urls))
]