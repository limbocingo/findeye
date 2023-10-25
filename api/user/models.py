"""
Models of `user` application.

[author: mrcingo]
"""


from django.contrib.auth.hashers import identify_hasher, make_password, check_password
from django.core.validators import MinLengthValidator
from django.db.models import *
from django.utils import timezone

from information.models import *

import random
import string


class User(Model):
    """
    This is user sensitive data that will be used by the alghorithm
    to find the best job.

    Data for the alghorithm:
        - Respond Time: Avg respond time in seconds. (Integer)
        - Jobs: Jobs he done or it has on pending. (ManyToMany of jobs.Job model.)
        - Categories: Things that knows. (ManyToMany of jobs.Category model.)
        - Badges: Achievements. (ManyToMany of achievements.Badge model.)
        - Languages: Langs he knows. (ManyToMany of achievements.Language model.)
        - Client: He's a project, company, startup... That payed for our service. (Boolean)

    Permissions system:
        - Groups: ManyToMany of Group model.
        - Permissions: ManyToMany of Permission model.
    """

    username = CharField(max_length=150, unique=True, validators=[
        MinLengthValidator(4)])
    password = CharField(max_length=128, validators=[
        MinLengthValidator(8)])

    discord_id = TextField(unique=True)
    sid = TextField(default=''.join(random.choices(string.ascii_letters + string.digits, k=32)))

    title = TextField(max_length=50, validators=[
                      MinLengthValidator(8)], blank=True)
    description = TextField(max_length=160, validators=[
                            MinLengthValidator(40)], blank=True)

    languages = ManyToManyField(Language, blank=True)
    badges = ManyToManyField(Badge, blank=True)
    avg_response_time = IntegerField(default=0)

    administrator = BooleanField(default=False)
    client = BooleanField(default=False)

    date_joined = DateTimeField(default=timezone.now)

    def check_password(self, input):
        return check_password(input, self.password)

    def save(self, *args, **kwargs) -> None:
        try:
            identify_hasher(self.password)
        except ValueError:
            self.password = make_password(self.password)

        super().save(*args, **kwargs)
