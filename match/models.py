from django.db import models
from team.models import Team
from competition.models import Competition
from datetime import date


class Match(models.Model):
    competition = models.ForeignKey(Competition, related_name="competition")
    homeTeam = models.ForeignKey(Team, related_name="home")
    awayTeam = models.ForeignKey(Team, related_name="away")
    match_time = models.DateField(default=date.today)

    def __str__(self):
        return self.homeTeam.team_name + ' vs ' + self.awayTeam.team_name + ' (' + str(self.match_time) + ')'