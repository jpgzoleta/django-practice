from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
