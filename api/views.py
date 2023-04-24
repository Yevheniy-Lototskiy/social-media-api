from rest_framework import viewsets

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
