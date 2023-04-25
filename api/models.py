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
    profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    content = models.TextField()
    post_picture = models.ImageField(upload_to="post_pictures/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(
        "Profile",
        on_delete=models.CASCADE,
        related_name="posts"
    )
    hashtag = models.CharField(max_length=62, blank=True)

    class Meta:
        ordering = ["-created_at"]

    # def save(self, *args, **kwargs):
    #     if self.hashtag and not self.hashtag.startswith("#"):
    #         self.hashtag = f"#{self.hashtag}"
    #
    #     super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        tags = ""

        if self.hashtag:
            for tag in self.hashtag.split():
                if not tag.startswith("#"):
                    tags += f" #{tag}"

        self.hashtag = tags.strip()

        super().save(*args, **kwargs)
