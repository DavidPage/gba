from __future__ import unicode_literals
from match.models import Match
from market.models import Market
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Trade(models.Model):
    match = models.ForeignKey(Match, related_name="match")
    market = models.ForeignKey(Market, related_name="login")
    invested = models.DecimalField(max_digits=10, decimal_places=2)
    profitLoss = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User)

    # user = models.ForeignKey(User)


    def __str__(self):
        return self.invested

    def divide(self):
        return (int(self.profitLoss) * 100) / int(self.invested)

    def owner(self):
        return self.user
