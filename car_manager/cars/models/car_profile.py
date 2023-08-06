from django.contrib.auth import get_user_model
from django.core import validators

from django.db import models
from car_manager.common.validators import DataValidator, exact_vin_length

UserModel = get_user_model()


class CarsModel(models.Model):
    MIN_LEN_NUMBER_OF_VEHICLE = 7
    MAX_LEN_PLATE_NUMBER_OF_VEHICLE = 8
    MAX_LEN_OF_VIN_NUMBER = 17

    ALFA_ROMEO = 'Alfa Romeo'
    ASTON_MARTIN = 'Aston Martin'
    AUDI = 'Audi'
    BENTLEY = 'Bentley'
    BMW = 'BMW'
    BUGATTI = 'Bugatti'
    CITROEN = 'Citroen'
    DACIA = 'Dacia'
    FORD = 'Ford'
    FIAT = 'Fiat'
    MERCEDES = 'Mercedes-Benz'
    MITSUBISHI = 'Mitsubishi'
    OPEL = 'Opel'
    PEUGEOT = 'Peugeot'
    VOLKSWAGEN = 'VolksWagen'

    CAR = (
        (ALFA_ROMEO, ALFA_ROMEO),
        (ASTON_MARTIN, ASTON_MARTIN),
        (AUDI, AUDI),
        (BENTLEY, BENTLEY),
        (BMW, BMW),
        (CITROEN, CITROEN),
        (DACIA, DACIA),
        (FORD, FORD),
        (FIAT, FIAT),
        (MERCEDES, MERCEDES),
        (MITSUBISHI, MITSUBISHI),
        (OPEL, OPEL),
        (PEUGEOT, PEUGEOT),
        (VOLKSWAGEN, VOLKSWAGEN),

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
        max_length=MAX_LEN_OF_VIN_NUMBER,
        unique=True,
        null=False,
        blank=False,
        validators=(exact_vin_length, DataValidator('VIN number'),)

    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        self.vin_number = self.vin_number.upper()
        self.plate_number = self.plate_number.upper()
        super(CarsModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ['car_name', 'plate_number']
        verbose_name_plural = 'My Cars'
