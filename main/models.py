from django.db import models
import uuid


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    amount = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    description = models.TextField(null=True)