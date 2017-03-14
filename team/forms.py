from django import forms

from models import Team

#estes nomes de atributos teem que bater com os nomes dos atributos do model
class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team_name']
        #competition = forms.ChoiceField
        #homeTeam = forms.ChoiceField
        #awayTeam = forms.CharField
        #match_time = forms.DateTimeField()