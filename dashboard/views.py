from django.shortcuts import render
from trade.models import Trade
from match.models import Match
from models import Bank
from django.http import HttpResponseRedirect

def monthname(month_num):
    names = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
             7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
    return names[month_num]


def sumByMonth(tradeCollection):
    totalOfMonth = 0.0

    for trade in tradeCollection:
        totalOfMonth = totalOfMonth + float(trade.profitLoss)

    return totalOfMonth

def initialAmount(request):
    return render(request, 'dashboard/new.html')

def insertInitialAmount(request):
    print 'bank.insert'
    if request.method == 'POST':
        b = Bank(initialAmount=request.POST["initialAmount"])
        b.save()
    return HttpResponseRedirect('/')

def index(request):
    print 'dashboard.index'

    allTrades = Trade.objects.all()

    # Step 1: Create a DataPool with the data we want to retrieve.
    januaryMatches = Match.objects.filter(match_time__month=1).values('id')
    januarySum = sumByMonth(Trade.objects.filter(match_id__in=januaryMatches))

    februaryMatches = Match.objects.filter(match_time__month=2).values('id')
    februarySum = sumByMonth(Trade.objects.filter(match_id__in=februaryMatches))

    marchMatches = Match.objects.filter(match_time__month=3).values('id')
    marchSum = sumByMonth(Trade.objects.filter(match_id__in=marchMatches))

    aprilMatches = Match.objects.filter(match_time__month=4).values('id')
    aprilSum = sumByMonth(Trade.objects.filter(match_id__in=aprilMatches))

    mayMatches = Match.objects.filter(match_time__month=5).values('id')
    maySum = sumByMonth(Trade.objects.filter(match_id__in=mayMatches))

    juneMatches = Match.objects.filter(match_time__month=6).values('id')
    juneSum = sumByMonth(Trade.objects.filter(match_id__in=juneMatches))

    julyMatches = Match.objects.filter(match_time__month=7).values('id')
    julySum = sumByMonth(Trade.objects.filter(match_id__in=julyMatches))

    augustMatches = Match.objects.filter(match_time__month=8).values('id')
    augustSum = sumByMonth(Trade.objects.filter(match_id__in=augustMatches))

    septemberMatches = Match.objects.filter(match_time__month=9).values('id')
    septemberSum = sumByMonth(Trade.objects.filter(match_id__in=septemberMatches))

    octoberMatches = Match.objects.filter(match_time__month=10).values('id')
    octoberSum = sumByMonth(Trade.objects.filter(match_id__in=octoberMatches))

    novemberMatches = Match.objects.filter(match_time__month=11).values('id')
    novemberSum = sumByMonth(Trade.objects.filter(match_id__in=novemberMatches))

    decemberMatches = Match.objects.filter(match_time__month=12).values('id')
    decemberSum = sumByMonth(Trade.objects.filter(match_id__in=decemberMatches))

    tradesByMonthCollection = [
         januarySum,
         februarySum,
         marchSum,
         aprilSum,
         maySum,
         juneSum,
         julySum,
         augustSum,
         septemberSum,
         octoberSum,
         novemberSum,
         decemberSum
     ]

    totalOfYear = 0
    totalInvestedYear = 0

    for trade in allTrades:
        totalOfYear = totalOfYear + trade.profitLoss
        totalInvestedYear = totalInvestedYear + trade.invested

    totalROIOfYear = float((totalInvestedYear * 100) / totalOfYear)

    currentBank = Bank.objects.first()
    currentBank = currentBank.initialAmount + totalOfYear

    context = {
        'totalOfYear': totalOfYear,
        'totalROIOfYear': totalROIOfYear,
        'tradesByMonthCollection': tradesByMonthCollection,
        'currentBank': currentBank,
    }
    # context = {'tradesByMonthCollection': tradesByMonthCollection}

    print(tradesByMonthCollection)

    return render(request, 'dashboard/index.html', context)
