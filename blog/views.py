from django.shortcuts import render
from blog.models import Post
from django.shortcuts import render_to_response
from django.template import RequestContext

def blog(request):
    queryset = Post.objects.all().order_by("-date")[:25]
    return render(request, 'blog/blog.html', {'queryset':queryset})

def get_post(request, id):
    blog = Post.objects.get(id=id)
    return render(request, 'blog/post.html', locals())
