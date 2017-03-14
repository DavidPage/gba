from django.shortcuts import render
from django.http import HttpResponseRedirect
from competition.models import Competition

# Create your views here.

def index(request):
    competitions = Competition.objects.all()
    context = {
        'allCompetitions': competitions
    }
    return render(request, 'competition/index.html', context)


def new(request):
    return render(request, 'competition/new.html', )


def insert(request):
    competition = Competition(competition_name=request.POST.get('competitionName'))
    competition.save()
    return HttpResponseRedirect('/Competition/')


def delete(request, id):
    competition = Competition.objects.get(pk=id)
    competition.delete()
    return HttpResponseRedirect('/Competition/')
