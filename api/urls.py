from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import UserViewSet, ProfileViewSet, PostViewSet

router = DefaultRouter()
router.register("users", UserViewSet)
router.register("profiles", ProfileViewSet)
router.register("posts", PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "users"
