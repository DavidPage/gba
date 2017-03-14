from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Bank(models.Model):
    initialAmount = models.DecimalField(max_digits=10, decimal_places=2)