from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='car_photos/', null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Sale(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sale_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Set the car availability to False when the sale is created
        if not self.pk:  # This is a new sale
            self.car.available = False
            self.car.save()  # Save the car with updated availability
        super().save(*args, **kwargs)  # Call the original save method

    @property
    def car_photo(self):
        return self.car.photo

    def __str__(self):
        return f"Sale of {self.car} to {self.customer} on {self.sale_date}"
