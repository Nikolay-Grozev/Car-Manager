from curses.ascii import isalnum
from django import forms
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

LEN_OF_VIN_NUMBER = 17


def exact_vin_length(value):
    length = LEN_OF_VIN_NUMBER
    if len(value) != length:
        raise ValidationError(f"The VIN-number must be exactly {length} characters long.")


def validate_date_range(start_date, end_date):
    if start_date and end_date and start_date >= end_date:
        raise forms.ValidationError("Start date must be less than end date.")


@deconstructible
class MinDateValidator:
    def __init__(self, min_date):
        self.min_date = min_date

    def __call__(self, value):
        if value < self.min_date:
            raise ValidationError(f'Date must be greater than {self.min_date}')


@deconstructible
class MaxDateValidator:
    def __init__(self, max_date):
        self.max_date = max_date

    def __call__(self, value):
        if self.max_date < value:
            raise ValidationError(f'Date must be earlier than {self.max_date}')


@deconstructible
class DataValidator:
    def __init__(self, field_name):
        self.field_name = field_name

    def __call__(self, value):
        for x in value:
            if not isalnum(x):
                raise ValidationError(f'The {self.field_name} must contain only alphas and numbers.')
