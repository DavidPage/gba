from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db.models.fields import CharField

class Market(models.Model):
    market_name = CharField(max_length=20)

    def __str__(self):
        return self.market_name