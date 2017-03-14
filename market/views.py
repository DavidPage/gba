from django.shortcuts import render
from .models import Market
from django.http.response import HttpResponseRedirect


def markets(request):
    allMarkets = Market.objects.all()
    context = {'allMarkets': allMarkets}
    return render(request, 'market/index.html', context)


def new(request):
    return render(request, 'market/new.html', )


def insert(request):
    market = Market(market_name = request.POST.get('marketName'))
    market.save()
    return HttpResponseRedirect('/Market/')


def delete(request, id):
    # If the form has been submitted...
    m = Market.objects.get(pk=id)
    m.delete()
    return HttpResponseRedirect('/Market/')