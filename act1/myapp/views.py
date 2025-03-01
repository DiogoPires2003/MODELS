from django.shortcuts import render,redirect
from myapp.models import Car, Sale, Customer
from myapp.forms import CarForm, SaleForm
# Home page view

# View all cars
def cars(request):
    cars = Car.objects.all()
    return render(request, 'cars.html', {'cars': cars})

# View all sales
def sales(request):
    sales = Sale.objects.all()
    return render(request, 'sales.html', {'sales': sales})


def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cars')  # Redirect to the available cars page after successful submission
    else:
        form = CarForm()

    return render(request, 'addCar.html', {'form': form})


def sell_car(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Sold cars')  # Redirect to the sales page after successful submission
    else:
        form = SaleForm()

    return render(request, 'sellCar.html', {'form': form})

def customers(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})