from curses.ascii import isalnum
import re

from django.contrib.auth import get_user_model
from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.deconstruct import deconstructible

from car_manager.accounts.models import CarManagerUser
from car_manager.common.validators import DataValidator, exact_vin_length

UserModel = get_user_model()


class CarsModel(models.Model):
    MIN_LEN_NUMBER_OF_VEHICLE = 7
    MAX_LEN_PLATE_NUMBER_OF_VEHICLE = 8
    LEN_OF_VIN_NUMBER = 17

    OPEL = 'Opel'
    CITROEN = 'Citroen'
    BMW = 'BMW'

    CAR = (
        (OPEL, OPEL),
        (CITROEN, CITROEN),
        (BMW, BMW),

    )

    car_name = models.CharField(
        choices=CAR,
        null=False,
        blank=False,
    )

    plate_number = models.CharField(
        max_length=MAX_LEN_PLATE_NUMBER_OF_VEHICLE,
        unique=True,
        blank=False,
        null=False,
        verbose_name='Enter Plate Number',
        validators=(
            validators.MinLengthValidator(MIN_LEN_NUMBER_OF_VEHICLE),
            DataValidator('plate number')
        ),
    )

    vin_number = models.CharField(
        max_length=LEN_OF_VIN_NUMBER,
        unique=True,
        null=False,
        blank=False,
        validators=(exact_vin_length, DataValidator('VIN number'),)

    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name_plural = 'My Cars'
