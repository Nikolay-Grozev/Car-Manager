from django.core.validators import RegexValidator
from django.db import models


class Contact(models.Model):
    PHONE_NUMBER_MAX_LENGTH = 16
    PHONE_NUMBER_REGEX_PATTERN = r"^\+?1?\d{9,15}$"
    PHONE_NUMBER_ERROR_MESSAGE = "Phone number must be entered in the format: '+999999999'.Up to 15 digits is allowed"

    name = models.CharField(
        max_length=250,
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=PHONE_NUMBER_MAX_LENGTH,
        null=False,
        blank=False,
        validators=(
            RegexValidator(
                regex=PHONE_NUMBER_REGEX_PATTERN,
                message=PHONE_NUMBER_ERROR_MESSAGE,
            ),
        )
    )

    mode_of_contact = models.CharField(
        'Contact by', max_length=50,
        null=False,
        blank=False,
    )

    question_categories = models.CharField(
        'How can we help you?', max_length=50,
        null=False,
        blank=False,
    )

    message = models.TextField(
        max_length=3000,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.email
