from rest_framework import viewsets

from api.models import Profile, Post
from api.permissions import (
    IsProfileOwnerOrReadOnly,
    IsAuthorOrReadOnly
)
from api.serializers import (
    ProfileSerializer,
    ProfileDetailSerializer,
    PostSerializer
)
from user.models import User
from user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        """Retrieve the user with filters"""
        email = self.request.query_params.get("email")

        queryset = self.queryset

        if email:
            queryset = queryset.filter(email__icontains=email)

        return queryset.distinct()


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsProfileOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ["retrieve", "update", "create"]:
            return ProfileDetailSerializer

        return self.serializer_class

    def get_queryset(self):
        nickname = self.request.query_params.get("nickname")
        first_name = self.request.query_params.get("first_name")
        last_name = self.request.query_params.get("last_name")

        queryset = self.queryset

        if nickname:
            queryset = queryset.filter(nickname__icontains=nickname)

        if first_name:
            queryset = queryset.filter(first_name__icontains=first_name)

        if last_name:
            queryset = queryset.filter(last_name__icontains=last_name)

        return queryset


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        hashtag = self.request.query_params.get("hashtag")

        queryset = self.queryset

        if hashtag:
            queryset = queryset.filter(hashtag__icontains=hashtag)

        return queryset
