from django.shortcuts import render
from blog.models import Post
from django.shortcuts import render_to_response
from django.template import RequestContext
from master.models import EventTable

def listall(request):
    queryset = EventTable.objects.all().order_by("-id")[:25]
    return render(request, 'master/home.html', {'queryset':queryset})

