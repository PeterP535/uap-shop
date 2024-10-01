from django.db import models
from django.utils import timezone
import uuid

class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    amount = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    description = models.TextField(null=True)
    genre = models.CharField(max_length=100, null=True)
    platform = models.CharField(max_length=50, null=True)
    date_added = models.DateTimeField(default=timezone.now)  # Default to current timestamp for existing items

class ShoppingCart(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
