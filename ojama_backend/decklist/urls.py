from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'decklisturls', views.DecklistUrlViewSet, basename='decklisturl')

urlpatterns = [
    path('', include(router.urls)),
]