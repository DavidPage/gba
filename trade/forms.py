from django import forms
from .models import Trade

class TradeForm(forms.ModelForm):
    class Meta:
        model = Trade
        fields = ['match', 'market', 'invested', 'profitLoss']
        #match = forms.ChoiceField
        #market = forms.ChoiceField
        #invested = forms.CharField
        #profitLoss = forms.CharField(max_length=10)

