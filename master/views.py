from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .models import Person
from .forms import PersonForm

def register(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PersonForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            model_instance = form.save(commit=False)
            model_instance.save()

            return HttpResponseRedirect('/thanks/')

    else:
        form = PersonForm()
    return render(request, 'master/register.html', {'form' : form})

def thanks(request):
    return render(request, 'master/thanks.html')