from django.contrib import admin
# Register your models here.
from .models import City, Route, TouristPlace # Importa tus modelos


admin.site.register(City)
admin.site.register(Route)
admin.site.register(TouristPlace)