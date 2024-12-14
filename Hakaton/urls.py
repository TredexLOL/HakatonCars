from django.contrib import admin
from django.urls import path

from cars.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('maintenance/', maintenance, name='maintenance'),
    path('repair/', repair, name='repair'),
    path('price/', price, name='price'),
    path('locations/', locations, name='locations')
]
