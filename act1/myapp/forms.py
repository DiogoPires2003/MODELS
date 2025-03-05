
from django import forms
from .models import Car, Sale, Customer


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'year', 'price', 'km', 'photo']

    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)

        # Explicitly setting all fields as required
        self.fields['brand'].required = True
        self.fields['model'].required = True
        self.fields['year'].required = True
        self.fields['price'].required = True
        self.fields['km'].required = True
        self.fields['photo'].required = True

        # Adding Bootstrap class to form fields for better styling
        self.fields['brand'].widget.attrs.update({'class': 'form-control'})
        self.fields['model'].widget.attrs.update({'class': 'form-control'})
        self.fields['year'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})
        self.fields['km'].widget.attrs.update({'class': 'form-control'})
        self.fields['photo'].widget.attrs.update({'class': 'form-control'})

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['car', 'customer', 'total_price']

    def __init__(self, *args, **kwargs):
        super(SaleForm, self).__init__(*args, **kwargs)
        self.fields['car'].queryset = Car.objects.filter(available=True)

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone']

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        self.fields['phone'].required = True
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})