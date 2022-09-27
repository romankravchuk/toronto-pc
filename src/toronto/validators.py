from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class UserPhoneValidator(validators.RegexValidator):
    regex = r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$"
    message = _("Enter a valid phone number. This value may contain only numbers")
    flags = 0
