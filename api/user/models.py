from django.contrib.auth.hashers import make_password, identify_hasher
from django.core.validators import MinLengthValidator
from django.db.models import *
from django.utils import timezone


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

    username = CharField(max_length=150, unique=True)
    password = CharField(max_length=128)

    discord_id = TextField()

    title = TextField(max_length=50, validators=[
                      MinLengthValidator(8)])
    description = TextField(max_length=160, validators=[
                            MinLengthValidator(40)])

    languages = ManyToManyField(Language)
    skills = ManyToManyField(Skill)

    badges = ManyToManyField(Badge, blank=True)

    administrator = BooleanField(default=False)
    premium = BooleanField(default=False)

    date_joined = DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs) -> None:
        try:
            identify_hasher(self.password)
        except ValueError:
            self.password = make_password(self.password)

        super().save(*args, **kwargs)
