from django.contrib.auth import get_user_model
from rest_framework import serializers

from api.models import Profile, Post
from user.serializers import UserSerializer


class ProfileSerializer(serializers.ModelSerializer):
    posts_count = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = (
            "id",
            "nickname",
            "full_name",
            "bio",
            "profile_picture",
            "posts_count"
        )

    @staticmethod
    def get_posts_count(obj):
        return Post.objects.filter(profile_id=obj.id).count()


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ("id", "profile", "content", "post_picture", "created_at")


class ProfileDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "nickname",
            "first_name",
            "last_name",
            "bio",
            "profile_picture",
            "posts"
        )


