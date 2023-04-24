from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import UserViewSet, ProfileViewSet

router = DefaultRouter()
router.register("users", UserViewSet)
router.register("profiles", ProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "user"
