from django.shortcuts import render,redirect
from myapp.models import Car, Sale
from myapp.forms import CarForm
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


def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cars')  # Redirect to the available cars page after successful submission
    else:
        form = CarForm()

    return render(request, 'addCar.html', {'form': form})