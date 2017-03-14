from __future__ import unicode_literals
from django.db import models
from django.db.models.fields import CharField


class Team(models.Model):
    team_name = CharField(max_length=20)

    def __str__(self):
        return self.team_name