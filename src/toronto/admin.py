from django.contrib import admin

from . import models


@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "phone",
        "last_name",
        "first_name",
        "email",
        "date_joined",
        "last_login",
    )
    fields = [("phone", "password"), ("last_name", "first_name"), "email", "address"]


@admin.register(models.Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "is_avaiable", "price")


@admin.register(models.ComponentImage)
class ComponentImageAdmin(admin.ModelAdmin):
    list_display = ("id", "component", "path", "is_main")
