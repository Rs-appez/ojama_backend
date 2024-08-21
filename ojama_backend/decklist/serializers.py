from .models import DecklistUrl, LastBanlist
from rest_framework import serializers

class DecklistUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = DecklistUrl
        fields = '__all__'

class BanlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = LastBanlist
        fields = '__all__'