from .models import DecklistUrl
from rest_framework import serializers

class DecklistUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = DecklistUrl
        fields = ['url']