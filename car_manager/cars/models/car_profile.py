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
    BUICK = 'Buick'
    CADILLAC = 'Cadillac'
    CHEVROLET = 'Chevrolet'
    CHRYSLER = 'Chrysler'
    CITROEN = 'Citroen'
    DACIA = 'Dacia'
    DAEWOO = 'Daewoo'
    DAIHATSU = 'Daihatsu'
    DATSUN = 'Datsun'
    DODGE = 'Dodge'
    DS = 'DS'
    FERRARI = 'Ferrari'
    FIAT = 'Fiat'
    FORD = 'Ford'
    GMC = 'GMC'
    GREATWALL = 'Great Wall'
    HAVAL = 'Haval'
    HOLDEN = 'Holden'
    HONDA = 'Honda'
    HUMMER = 'Hummer'
    HYUNDAI = 'Hyundai'
    ISUZU = 'Isuzu'
    JAGUAR = 'Jaguar'
    JEEP = 'JEEP'
    KIA = 'Kia'
    KOENIGSEGG = 'Koenigsegg'
    LAMBORGHINI = 'Lamborghini'
    LANCIA = 'Lancia'
    LANDROVER = 'Land Rover'
    LEXUS = 'Lexus'
    LOTUS = 'Lotus'
    MASERATI = 'Maserati'
    MAYBACH = 'Maybach'
    MAZDA = 'Mazda'
    MCLAREN = 'McLaren'
    MERCEDES = 'Mercedes-Benz'
    MINI = 'MINI'
    MITSUBISHI = 'Mitsubishi'
    NISSAN = 'Nissan'
    OPEL = 'Opel'
    PEUGEOT = 'Peugeot'
    PONTIAC = 'Pontiac'
    PORSCHE = 'Porsche'
    RENAULT = 'Renault'
    ROVER = 'Rover'
    SAAB = 'Saab'
    SEAT = 'Seat'
    SKODA = 'Skoda'
    SMART = 'Smart'
    SUBARU = 'Subaru'
    SUZUKI = 'Suzuki'
    TESLA = 'Tesla'
    TOYOTA = 'Toyota'
    TVR = 'TVR'
    VAUXHALL = 'Vauxhall'
    VOLKSWAGEN = 'VolksWagen'
    VOLVO = 'Volvo'
    OTHER = 'Other'

    CAR = (
        (ALFA_ROMEO, ALFA_ROMEO),
        (ASTON_MARTIN, ASTON_MARTIN),
        (AUDI, AUDI),
        (BENTLEY, BENTLEY),
        (BMW, BMW),
        (BUICK, BUICK),
        (BUGATTI, BUGATTI),
        (CADILLAC, CADILLAC),
        (CITROEN, CITROEN),
        (CHRYSLER, CHRYSLER),
        (CHEVROLET, CHEVROLET),
        (DACIA, DACIA),
        (DAEWOO, DAEWOO),
        (DAIHATSU, DAIHATSU),
        (DATSUN, DATSUN),
        (DS, DS),
        (DODGE, DODGE),
        (FERRARI, FERRARI),
        (FIAT, FIAT),
        (FORD, FORD),
        (GMC, GMC),
        (GREATWALL, GREATWALL),
        (HAVAL, HAVAL),
        (HOLDEN, HOLDEN),
        (HONDA, HONDA),
        (HUMMER, HUMMER),
        (HYUNDAI, HYUNDAI),
        (ISUZU, ISUZU),
        (JAGUAR, JAGUAR),
        (JEEP, JEEP),
        (KIA, KIA),
        (KOENIGSEGG, KOENIGSEGG),
        (LAMBORGHINI, LAMBORGHINI),
        (LANCIA, LANCIA),
        (LANDROVER, LANDROVER),
        (LEXUS, LEXUS),
        (LOTUS, LOTUS),
        (MASERATI, MASERATI),
        (MAYBACH, MAYBACH),
        (MAZDA, MAZDA),
        (MCLAREN, MCLAREN),
        (MERCEDES, MERCEDES),
        (MINI, MINI),
        (MITSUBISHI, MITSUBISHI),
        (NISSAN, NISSAN),
        (OPEL, OPEL),
        (PEUGEOT, PEUGEOT),
        (PONTIAC, PONTIAC),
        (PORSCHE, PORSCHE),
        (RENAULT, RENAULT),
        (ROVER, ROVER),
        (SAAB, SAAB),
        (SKODA, SKODA),
        (SMART, SMART),
        (SUBARU, SUBARU),
        (SUZUKI, SUZUKI),
        (TESLA, TESLA),
        (TOYOTA, TOYOTA),
        (TVR, TVR),
        (TESLA, TESLA),
        (VOLKSWAGEN, VOLKSWAGEN),
        (VOLVO, VOLVO),
        (OTHER, OTHER),

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
