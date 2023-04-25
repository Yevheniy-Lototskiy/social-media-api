from django.contrib.auth import get_user_model
from rest_framework import serializers

from api.models import Profile, Post
from user.serializers import UserSerializer


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = (
            "id",
            "nickname",
            "full_name",
            "bio",
            "profile_picture"
        )

class ProfileDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "nickname",
            "first_name",
            "last_name",
            "bio",
            "profile_picture"
        )

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ("id", "content", "post_picture", "created_at")
