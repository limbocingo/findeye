from django.db.models import *


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
