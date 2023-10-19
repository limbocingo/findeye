from rest_framework.viewsets import ModelViewSet

from user.models import User
from user.v1.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'discord_id'
