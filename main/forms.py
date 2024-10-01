from django import forms
from main.models import Item, CartItem

class ProductForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "price", "description"]
        labels = {
            'name': 'Game Name',
            'amount': 'Quantity',
            'price': 'Price',
            'description': 'Description',
        }

class AddToCartForm(forms.Form):
    amount = forms.IntegerField(label="Amount", min_value=1, initial=1)  # Only ask for the amount