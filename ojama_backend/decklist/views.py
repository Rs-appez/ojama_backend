from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import DecklistUrlSerializer, BanlistSerializer
from .models import DecklistUrl, LastBanlist

class DecklistUrlViewSet(viewsets.ModelViewSet):
    queryset = DecklistUrl.objects.all()
    serializer_class = DecklistUrlSerializer
    permission_classes = [IsAuthenticated]


class BanlistViewSet(viewsets.ModelViewSet):
    queryset = LastBanlist.objects.all()
    serializer_class = BanlistSerializer
    permission_classes = [IsAuthenticated]