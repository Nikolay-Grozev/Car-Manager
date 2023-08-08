from django import forms
from django.contrib import admin

from car_manager.cars.models.car_profile import CarsModel


@admin.register(CarsModel)
class CarsModelAdmin(admin.ModelAdmin):
    list_display = (
        'car_name',
        'plate_number',
        'vin_number',
        'user',
    )

    readonly_fields = ('user',)

    def save_model(self, request, obj, form, change):
        try:
            if CarsModel.objects.filter(vin_number=obj.vin_number).exclude(pk=obj.pk).exists():
                raise forms.ValidationError("A car with this VIN number already exists.")

            if CarsModel.objects.filter(plate_number=obj.plate_number).exclude(pk=obj.pk).exists():
                raise forms.ValidationError("A car with this plate number already exists.")

            super().save_model(request, obj, form, change)
        except forms.ValidationError as ex:
            self.message_user(request, str(ex), level='error')
