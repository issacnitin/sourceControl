from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .models import Language
from .forms import WhatUserWants

def register(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserCreationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('thanks')
    else:
        form = UserCreationForm()
    return render(request, 'master/register.html', {'form' : form})

def thanks(request):
    return render(request, 'master/thanks.html')

def home(request):
    if not request.user.is_authenticated():
        return redirect('register')
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WhatUserWants(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if(Language.objects.filter(name=form.cleaned_data['language']).count()):
                p = Language.objects.get(name=form.cleaned_data['language'])
                #print("count = " + p.count)
                p.count += 1
                p.save()
            else:
                p = Language(name=form.cleaned_data['language'], count=1)
                p.save()
        query_results = Language.objects.all()
        return render(request, 'master/home.html', {'form' : form, 'query_results':query_results})
    else:
        form = WhatUserWants()
        query_results = Language.objects.all()
        return render(request, 'master/home.html', {'form' : form, 'query_results':query_results})
