from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',

            'discord_id',

            'title',
            'description',

            'languages',
            'skills',

            'jobs',
            'badges',

            'date_joined',

            'premium',
            'administrator',
        )

        read_only_fields = ('date_joined',
                            'administrator')
