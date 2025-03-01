
from django import forms
from .models import Car, Sale

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'year', 'price', 'km', 'photo']



class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['car', 'customer', 'total_price']

    def __init__(self, *args, **kwargs):
        super(SaleForm, self).__init__(*args, **kwargs)
        self.fields['car'].queryset = Car.objects.filter(available=True)