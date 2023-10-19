from django.contrib.auth.hashers import identify_hasher, make_password, check_password
from django.core.validators import MinLengthValidator
from django.db.models import *
from django.utils import timezone

import random
import string


class Language(Model):
    name = CharField(unique=True, max_length=64, validators=[
                     MinLengthValidator(8)], primary_key=True)


class Skill(Model):
    name = CharField(unique=True, max_length=64, validators=[
                     MinLengthValidator(8)], primary_key=True)
    approved = BooleanField(default=False)


class Badge(Model):
    name = CharField(unique=True, max_length=64, validators=[
                     MinLengthValidator(8)], primary_key=True)
    icon = TextField(blank=False)


class User(Model):
    """
    TODO: 
        - Respond Time: Avg respond time
        - Jobs: ManyToMany of Jobs model.
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
    skills = ManyToManyField(Skill, blank=True)

    badges = ManyToManyField(Badge, blank=True)

    administrator = BooleanField(default=False)
    premium = BooleanField(default=False)

    date_joined = DateTimeField(default=timezone.now)

    def check_password(self, input):
        return check_password(input, self.password)

    def save(self, *args, **kwargs) -> None:
        try:
            identify_hasher(self.password)
        except ValueError:
            self.password = make_password(self.password)

        super().save(*args, **kwargs)
