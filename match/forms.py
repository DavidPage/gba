from django import forms

from models import Match

#estes nomes de atributos teem que bater com os nomes dos atributos do model
class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['competition', 'homeTeam', 'awayTeam', 'match_time']
        #competition = forms.ChoiceField
        #homeTeam = forms.ChoiceField
        #awayTeam = forms.CharField
        #match_time = forms.DateTimeField()