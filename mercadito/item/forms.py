from django import forms
from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model=Item
        field=('category', 'name', 'description', 'price', 'image',)