from django.shortcuts import render
from gbauser.forms import LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/Dashboard')
                else:
                    print('The account has been disabled')
            else:
                print('The username and password were incorrect!')
                return render(request, 'gbauser/loginerror.html', {'request': request})

    else:
        form = LoginForm(request.POST)
        return render(request, 'gbauser/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")