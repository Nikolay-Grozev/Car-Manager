from django.db import models
import datetime
from car_manager.cars.models.car_profile import CarsModel
from car_manager.common.validators import MinDateValidator, MaxDateValidator


class ReminderModel(models.Model):
    MIN_DATE = datetime.date(1900, 1, 1)
    MAX_DATE = datetime.date(2100, 1, 1)

    INSURANCE = 'Insurance'
    PERIODIC_TECH_INSPECTIONS = 'Periodic tech inspections'
    TOOL_TAXES = 'Toll taxes'

    Reminder = (
        (INSURANCE, INSURANCE),
        (PERIODIC_TECH_INSPECTIONS, PERIODIC_TECH_INSPECTIONS),
        (TOOL_TAXES, TOOL_TAXES),

    )

    reminder_name = models.CharField(
        choices=Reminder,
        null=False,
        blank=False,
    )

    start_date = models.DateField(
        null=False,
        blank=False,
        validators=(
            MinDateValidator(MIN_DATE),
            MaxDateValidator(MAX_DATE),
        ),
    )

    end_date = models.DateField(
        null=False,
        blank=False,
        validators=(
            MinDateValidator(MIN_DATE),
            MaxDateValidator(MAX_DATE),
        ),
    )

    car = models.ForeignKey(
        CarsModel,
        on_delete=models.CASCADE,
    )
