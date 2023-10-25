"""
User application serializers.

[version: 1v]
"""


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
            'badges',

            'date_joined',

            'client',
            'administrator',
        )

        read_only_fields = ('date_joined',
                            'administrator',
                            'sid',)
