from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profiles"
    )
    nickname = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    # profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
