from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import DecklistUrlSerializer
from .models import DecklistUrl

class DecklistUrlViewSet(viewsets.ModelViewSet):
    queryset = DecklistUrl.objects.all()
    serializer_class = DecklistUrlSerializer
    permission_classes = [IsAuthenticated]