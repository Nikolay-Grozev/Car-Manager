from django import forms

from car_manager.cars.models.car_profile import CarsModel
from car_manager.common.bootstrap_mixin import BootstrapFormControl


class CarRegistrationForm(forms.ModelForm, BootstrapFormControl):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        super().apply_class_form_control(self.fields)

    def clean_plate_number(self):
        plate_number = self.cleaned_data['plate_number']
        return plate_number.upper()

    def clean_vin_number(self):
        vin_number = self.cleaned_data['vin_number']
        return vin_number.upper()

    def save(self, commit=True):
        car = super().save(commit=False)
        car.user = self.user
        if commit:
            car.save()
        return car

    class Meta:
        model = CarsModel
        exclude = ('user',)


class EditCarForm(forms.ModelForm, BootstrapFormControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super().apply_class_form_control(self.fields)

    def clean_plate_number(self):
        plate_number = self.cleaned_data['plate_number']
        return plate_number.upper()

    def clean_vin_number(self):
        vin_number = self.cleaned_data['vin_number']
        return vin_number.upper()

    class Meta:
        model = CarsModel
        fields = ('plate_number',)


class DeleteCarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        super().save(commit=commit)
        self.instance.delete()
        return self.instance

    class Meta:
        model = CarsModel
        fields = ()


class CarsAdminForm(forms.ModelForm):
    class Meta:
        model = CarsModel
        fields = '__all__'

    def clean_plate_number(self):
        plate_number = self.cleaned_data['plate_number']
        return plate_number.upper()

    def clean_vin_number(self):
        vin_number = self.cleaned_data['vin_number']
        return vin_number.upper()