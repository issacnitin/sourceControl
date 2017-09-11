from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

def listall(request):
    return render(request, 'master/home.html')