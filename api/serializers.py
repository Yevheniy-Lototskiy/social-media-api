from rest_framework import serializers

from api.models import Profile, Post
from user.serializers import UserSerializer


class ProfileSerializer(serializers.ModelSerializer):
    posts_count = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = (
            "id",
            "nickname",
            "full_name",
            "bio",
            "profile_picture",
            "posts_count",
            "followers_count",
        )

    @staticmethod
    def get_posts_count(obj):
        return Post.objects.filter(profile_id=obj.id).count()

    def get_followers_count(self, obj):
        return obj.user.following.count()


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            "id",
            "profile",
            "content",
            "post_picture",
            "created_at",
            "hashtag"
        )


class ProfileDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    posts = PostSerializer(many=True, read_only=True)
    following = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()

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
            "posts",
            "following",
            "followers"
        )

    def get_following(self, obj):
        return [follower.username for follower in obj.followers.all()]

    def get_followers(self, obj):
        return [
            followed_user.user.username for followed_user in obj.user.following.all()
        ]
