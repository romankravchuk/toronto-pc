from django.contrib import admin

from . import models


class ComponentImageInLine(admin.TabularInline):
    model = models.ComponentImage
    extra = 0


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
    inlines = [ComponentImageInLine]


@admin.register(models.ComponentImage)
class ComponentImageAdmin(admin.ModelAdmin):
    list_display = ("path", "component", "is_main")


@admin.register(models.Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ("category", "value")
