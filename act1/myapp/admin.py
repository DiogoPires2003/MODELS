from django.contrib import admin
from .models import Car, Customer, Sale

# Register the models so they appear in the Admin interface
admin.site.register(Customer)
admin.site.register(Sale)
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'price', 'available', 'photo')
    search_fields = ('brand', 'model')
