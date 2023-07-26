from django.contrib.auth import get_user_model
from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models

from car_manager.accounts.models import CarManagerUser

UserModel = get_user_model()

LEN_OF_VIN_NUMBER = 17


# def exact_vin_length(value):
#     length = LEN_OF_VIN_NUMBER
#     if len(value) != length:
#         raise ValidationError(f"The VIN-number must be exactly {length} characters long.")


class CarsModel(models.Model):
    MIN_LEN_NUMBER_OF_VEHICLE = 7
    MAX_LEN_PLATE_NUMBER_OF_VEHICLE = 8

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
        ),
    )

    vin_number = models.CharField(
        max_length=LEN_OF_VIN_NUMBER,
        unique=True,
        null=False,
        blank=False,

    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name_plural = 'My Cars'

