from django.urls import path
from myapp.views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cars, name='cars'),
    path('sales/', sales, name='Sold cars'),
    path('add_car/', add_car, name='add_car'),
    path('sell_car/', sell_car, name='sell_car'),
    path('customers/', customers, name='customers'),
    path('add_customer/', add_customer, name='add_customer'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

