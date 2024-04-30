from django.db import models

# Create your models here.
class DecklistUrl(models.Model):
    url = models.CharField(max_length=200)
    name = models.CharField(max_length=200,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    post_by = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} : {self.url}"