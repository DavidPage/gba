from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.template.context import RequestContext
from trade.models import Trade
from competition.models import Competition
from team.models import Team
from market.models import Market
from match.models import Match
from django.http import HttpResponseRedirect
from trade.forms import TradeForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def trades(request):
    #allTrades = Trade.objects.all()
    allTrades = Trade.objects.filter(user=request.user)

    totalOfYear = 0
    totalInvestedYear = 0
    totalROIOfYear = 0

    for trade in allTrades:
        totalOfYear = totalOfYear + trade.profitLoss
        totalInvestedYear = totalInvestedYear + trade.invested
        totalROIOfYear = totalROIOfYear + (trade.profitLoss * 100) / trade.invested

    context = {'allTrades': allTrades, 'totalOfYear': totalOfYear, 'totalROIOfYear': totalROIOfYear}
    return render(request, 'trade/index.html', context)


def filterByMonth(request, id):
    print("id: " + id)
    allMonthlyMatches = Match.objects.filter(match_time__month = id).values('id')
    print(allMonthlyMatches)
    allTrades = Trade.objects.filter(user=request.user, match_id__in=allMonthlyMatches)

    totalOfMonth = 0
    totalROIOfMonth = 0

    for trade in allTrades:
        totalOfMonth = totalOfMonth + trade.profitLoss
        totalROIOfMonth = totalROIOfMonth + (trade.profitLoss * 100) / trade.invested

        print ("divide: " + str(trade.divide()))

    context = {'allTrades': allTrades, 'totalOfMonth': totalOfMonth, 'totalROIOfMonth': totalROIOfMonth}
    return render(request, 'trade/index.html', context)


def populatedb(request):

    myTeams = ['Real Madrid', 'Barcelona']
    myCompetitions = ['La liga', 'English Premier League']
    myMarkets = ['Match Odds', 'Half Time']

    for market in myMarkets:
        try:
            Market.objects.get(market_name=market)
            print("Encontrado o market " + market)
        except ObjectDoesNotExist:
            print("A criar o market " + market)
            x = Market(
                market_name=market
             )
            x.save()


    for competition in myCompetitions:
        try:
            Competition.objects.get(competition_name=competition)
            print("Encontrada a competition " + competition)
        except ObjectDoesNotExist:
                print("A criar a competition " + competition)
                x = Competition(
                    competition_name=competition
                 )
                x.save()

    for team in myTeams:
        try:
            Team.objects.get(team_name=team)
            print("Encontrada a Team " + team)
        except ObjectDoesNotExist:
            print("A criar a team " + team)
            x = Team(
                team_name=team
             )
            x.save()

    return HttpResponseRedirect('/Trade/')


def new(request):
    form = TradeForm()
    return render(request, 'trade/new.html', {'form': form})


@csrf_protect
def insert(request):
    if request.method == "POST":
        form = TradeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return HttpResponseRedirect('/Trade/')
        else:
            print form.errors  # To see the form errors in the console.

def delete(request, id):
    trade = Trade.objects.get(pk=id)
    trade.delete()
    return HttpResponseRedirect('/Trade/')

