from django import forms
from .models import Item

INPUT_CLASES = 'w-full py-4 px-6 rounded-xl border-xl'

class NewItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('category', 'name', 'description', 'price', 'image', 'inventory', 'date',)
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASES,
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASES,
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASES,
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASES,
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASES,
            }),
            'inventory': forms.TextInput(attrs={
                'class': INPUT_CLASES,
            }),
            'date': forms.DateInput(attrs={
                'class': INPUT_CLASES,
            }),
        }