from django.shortcuts import render
from models import Team
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    print 'team.index'
    allTeams = Team.objects.all()
    context = {'allTeams': allTeams}

    return render(request, 'index.html', context)

def new(request):
    print 'team.new'
    return render(request, 'new.html')

def insert(request):
    print 'team.insert'
    if request.method == 'POST':
        t = Team(team_name=request.POST["teamName"])
        t.save()
    return HttpResponseRedirect('/Team/')

def delete(request,id):
    team = Team.objects.get(pk=id)
    team.delete()
    return HttpResponseRedirect('/Team/')