from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BreedViewSet, KittenViewSet

router = DefaultRouter()
router.register(r'breeds', BreedViewSet)
router.register(r'kittens', KittenViewSet, basename='kitten')

urlpatterns = [
    path('', include(router.urls)),
]
