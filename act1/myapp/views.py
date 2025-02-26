from django.shortcuts import render
from myapp.models import Car, Sale

# Home page view
def home(request):
    return render(request, 'index.html')

# View all cars
def cars(request):
    cars = Car.objects.all()
    return render(request, 'cars.html', {'cars': cars})

# View all sales
def sales(request):
    sales = Sale.objects.all()
    return render(request, 'sales.html', {'sales': sales})

# Contact page view (basic)
