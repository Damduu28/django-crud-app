from django import forms
from .models import Crud

class CrudForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={"onChange": "showImage(this)", "name": "image", "id":"c__img"}))
    class Meta:
        model = Crud
        fields = ['image', 'title', 'price']
        
        widgets = {
            'title': forms.TextInput(attrs={"placeholder": "Product Title"}),
            'price': forms.TextInput(attrs={"placeholder": "Product Price"}),
        }