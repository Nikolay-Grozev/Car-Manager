import django.contrib.auth.models as auth_model
from django.core import exceptions
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models

from car_manager.accounts.manager import AppUserManager
from car_manager.common.validators import validate_only_letters


# TODO create function with max MB size image_url

# def validate_only_letters(value):
#     for ch in value:
#         if not ch.isalpha():
#             raise exceptions.ValidationError("The name should contain only letters!")


class CarManagerUser(auth_model.AbstractBaseUser, auth_model.PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    USERNAME_FIELD = 'email'

    objects = AppUserManager()


class ProfileDetails(models.Model):
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 20
    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 20
    PHONE_NUMBER_MAX_LENGTH = 16
    PHONE_NUMBER_REGEX_PATTERN = r"^\+?1?\d{9,15}$"
    PHONE_NUMBER_ERROR_MESSAGE = "Phone number must be entered in the format: '+999999999'.Up to 15 digits is allowed"

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            validate_only_letters,
        )
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    phone_number = models.CharField(
        max_length=PHONE_NUMBER_MAX_LENGTH,
        null=True,
        blank=True,
        validators=(
            RegexValidator(
                regex=PHONE_NUMBER_REGEX_PATTERN,
                message=PHONE_NUMBER_ERROR_MESSAGE
            ),
        )
    )

    user = models.OneToOneField(
        CarManagerUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    @property
    def full_name(self):
        if not self.first_name or not self.last_name:
            return f"No name"
        return f"{self.first_name} {self.last_name}"

