# Generated by Django 4.2.3 on 2023-08-04 19:12

import car_manager.common.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carsmodel',
            options={'ordering': ['car_name', 'plate_number'], 'verbose_name_plural': 'My Cars'},
        ),
        migrations.AlterField(
            model_name='carsmodel',
            name='car_name',
            field=models.CharField(choices=[('Opel', 'Opel'), ('Citroen', 'Citroen'), ('BMW', 'BMW'), ('Mercedes-Benz', 'Mercedes-Benz'), ('Peugeot', 'Peugeot')]),
        ),
        migrations.AlterField(
            model_name='carsmodel',
            name='plate_number',
            field=models.CharField(max_length=8, unique=True, validators=[django.core.validators.MinLengthValidator(7), car_manager.common.validators.DataValidator('plate number')], verbose_name='Enter Plate Number'),
        ),
        migrations.AlterField(
            model_name='carsmodel',
            name='vin_number',
            field=models.CharField(max_length=17, unique=True, validators=[car_manager.common.validators.exact_vin_length, car_manager.common.validators.DataValidator('VIN number')]),
        ),
    ]
