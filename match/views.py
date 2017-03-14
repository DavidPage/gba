from django.shortcuts import render
from match.models import Match
from django.http.response import HttpResponseRedirect
from forms import MatchForm


def match(request):
    matches = Match.objects.all()
    context = {'allMatches': matches}
    return render(request, 'match/index.html', context)


def new(request):
    form = MatchForm()
    return render(request, 'match/new.html', {'form': form})
    # return HttpResponseRedirect('/Match/')


def insert(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = MatchForm(request.POST)
        if form.is_valid():
            print('validform')
            post = form.save(commit=True)
            post.save()
            return HttpResponseRedirect('/Match/')
        else:
            print('not valid')
            return HttpResponseRedirect('/Match/')


def delete(request, id):
    print('valid: ' + id)
    m = Match.objects.get(pk=id)
    m.delete()
    return HttpResponseRedirect('/Match/')
