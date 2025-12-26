from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {
            'item_name': forms.TextInput(attrs={'placeholder':'e.g Margherita Pizza',"required":True}),
            'item_desec': forms.TextInput(attrs={'placeholder':'e.g Fresh and Cheesy ',"required":True}),
            'item_price': forms.NumberInput(attrs={'placeholder':'100',"required":True}),
            'item_image': forms.URLInput(attrs={'placeholder':'https://www.google.com',"required":False}),
            # 'item_name': forms.TextInput(attrs={'class':'form-control'}),
            # 'item_desc': forms.Textarea(attrs={'class': 'form-control'}),
            # 'item_price': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'item_image': forms.URLInput(attrs={'class': 'form-control'}),
        }
