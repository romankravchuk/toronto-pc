from django.urls import path, include
from django.contrib import admin
from rest_framework import routers

from toronto import views


router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
