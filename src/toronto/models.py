from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import models
from django.core.mail import send_mail

from . import managers, validators


class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_validator = validators.UserPhoneValidator()

    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    phone = models.CharField(
        _("phone"),
        max_length=20,
        unique=True,
        help_text=_("Required."),
        validators=[phone_validator],
        error_messages={"unique": _("A user with that phone number already exists.")},
    )
    address = models.CharField(_("address"), max_length=100, blank=True)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = managers.CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        full_name = f"{self.last_name} {self.first_name}"
        return full_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, **kwargs)
