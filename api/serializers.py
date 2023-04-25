from rest_framework import serializers

from api.models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = (
            "id",
            "nickname",
            "first_name",
            "last_name",
            "bio",
            "profile_picture"
        )

class ProfileDetailSerializer(ProfileSerializer):

    class Meta:
        model = Profile
        fields = (
            "id",
            # "user",
            # "nickname",
            # "first_name",
            # "last_name",
            # "bio",
            # "profile_picture"
        )
