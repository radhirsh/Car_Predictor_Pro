from django.contrib import admin
from .models import VehiclePost,BuyVehicle,Car
from .forms import CarForm

admin.site.register(VehiclePost)
admin.site.register(BuyVehicle)
# admin.site.register(CarForm)
# admin.site.register(CHOICES)
# admin.site.register(BuyingCarForm)

class CarAdmin(admin.ModelAdmin):
    form = CarForm

admin.site.register(Car, CarAdmin)

