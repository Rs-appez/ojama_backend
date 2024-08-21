from django.contrib import admin
from .models import DecklistUrl, LastBanlist

# Register your models here.
admin.site.register(DecklistUrl)
admin.site.register(LastBanlist)