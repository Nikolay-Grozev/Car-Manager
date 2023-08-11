from django.contrib import admin

from car_manager.cars.forms import CarsAdminForm
from car_manager.cars.models.car_profile import CarsModel


@admin.register(CarsModel)
class CarsModelAdmin(admin.ModelAdmin):
    form = CarsAdminForm
    list_display = (
        'car_name',
        'plate_number',
        'vin_number',
        'user',
    )

    readonly_fields = ('user',)

