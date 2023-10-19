from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',

            'discord_id',
            'sid',

            'title',
            'description',

            'languages',
            'skills',

            'badges',

            'date_joined',

            'premium',
            'administrator',
        )

        read_only_fields = ('date_joined',
                            'administrator',
                            'sid',)
