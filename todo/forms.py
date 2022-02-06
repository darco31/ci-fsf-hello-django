from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    """
    pass
    """
    class Meta:
        """
        pass
        """
        model = Item
        fields = ['name', 'done']
