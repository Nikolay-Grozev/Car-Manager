from django.contrib import admin

from car_manager.cars.models.car_profile import CarsModel


@admin.register(CarsModel)
class CarsModelAdmin(admin.ModelAdmin):
    pass
