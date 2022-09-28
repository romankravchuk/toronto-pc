from uuid import uuid4
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from . import managers


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    phone = PhoneNumberField(
        verbose_name=_("phone number"),
        region="RU",
        max_length=20,
        unique=True,
        help_text=_("Required. Must start with '+7' and contains 11 digits."),
        error_messages={"unique": _("A user with that phone number already exists.")},
    )
    address = models.CharField(_("address"), max_length=100, blank=True)

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = managers.CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["fist_name", "last_name", "email"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self) -> str:
        return self.get_full_name()

    def get_full_name(self):
        full_name = f"{self.last_name} {self.first_name}"
        return full_name

    def get_absolute_url(self):
        return reverse("user-detail", args=[str(self.id)])

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, **kwargs)


class Specification(models.Model):
    SPECIFICATION_CATEGORIES = [
        # TODO: add categories
        ("MOD", _("Model")),
        ("SOK", _("Socket")),
        ("YR", _("Release year")),
    ]

    category = models.CharField(
        _("category"), max_length=3, choices=SPECIFICATION_CATEGORIES, null=True
    )
    value = models.CharField(_("value"), max_length=100)

    class Meta:
        verbose_name = _("specification")
        verbose_name_plural = _("specifications")

    def __str__(self) -> str:
        return self.value


class Component(models.Model):
    CONFIGURATION_CATEGORIES = [
        ("GPU", _("Graphic Card")),
        ("CPU", _("Precessor")),
        ("MB", _("Motherboard")),
        ("RAM", _("Random Access Memory")),
        ("SSD", _("Solid State Drive")),
        ("HDD", _("Hard Drive Disk")),
        ("PS", _("Power Supply")),
        ("CS", _("Case")),
        ("FN", _("Fan")),
        ("OS", _("Operation System")),
        ("AV", _("Anti Virus")),
        ("MS", _("Mouse")),
        ("KB", _("Keyboard")),
        ("HP", _("Headphones")),
        ("MT", _("Monitor")),
        ("MP", _("Microphone")),
        ("GC", _("Gaming Chair")),
    ]

    name = models.CharField(_("name"), max_length=200, blank=True)
    category = models.CharField(
        _("category"), choices=CONFIGURATION_CATEGORIES, max_length=3
    )
    is_avaiable = models.BooleanField(_("is avaiable"), default=False)
    price = models.DecimalField(_("price"), max_digits=8, decimal_places=2, default=0)
    specifications = models.ManyToManyField(
        Specification, verbose_name=_("component specification")
    )

    def __str__(self):
        return self.name


class ComponentImage(models.Model):
    id = models.UUIDField(
        _("id"), primary_key=True, null=False, blank=False, default=uuid4()
    )
    component = models.ForeignKey(Component, on_delete=models.CASCADE, null=False)
    is_main = models.BooleanField(_("is main"), default=False)

    def get_directory_path(self, *args, **kwargs):
        filename = f"{uuid4()}.jpg"
        return f"components/component_{self.component.id}/{filename}"

    path = models.ImageField(
        _("image"),
        null=False,
        blank=False,
        upload_to=get_directory_path,
    )

    def __str__(self) -> str:
        return f"{self.component} image"


class Order(models.Model):
    ORDER_STATUSES = [("A", "Avaiable"), ("CL", "Closed"), ("CAN", "Canceled")]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    address = models.CharField(_("address"), null=False, max_length=200)
    prepaid = models.DecimalField(
        _("prepaid"), max_digits=8, decimal_places=2, default=0
    )
    price = models.DecimalField(_("price"), max_digits=8, decimal_places=2)
    status = models.CharField(_("status"), max_length=2, )

    date_created = models.DateTimeField(_("date created"), default=timezone.now)
    date_closed = models.DateTimeField(_("date closed"), null=True)
    date_canceled = models.DateTimeField(_("date canceled"), null=True)


class Configuration(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    components = models.ManyToManyField(
        Component, verbose_name=_("configuration components")
    )
    name = models.CharField(_("name"), max_length=150)
    summary = models.TextField(_("summary"), max_length=400)
    price = models.DecimalField(max_digits=8, decimal_places=2)
