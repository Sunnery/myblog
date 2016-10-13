# Create your views here.
# -*- coding: utf-8 -*-
from django.template import loader,Context
from django.http import HttpResponse
from myblog.models import BlogPost,Magic
from myblog.magnet import get_bt

def game(request):
    raise Exception

def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template('archive.html')
    c = Context({'posts': posts})
    return HttpResponse(t.render(c))

def index(request):
    posts = None
    t = loader.get_template('index.html')
    c = Context({'posts': posts})
    return HttpResponse(t.render(c))

def search(request):
    key = request.GET.get('key')
    if key == None:
        key = ''
        movies = []
    else:
        movies = get_bt(key)
        if movies:
            print 1
        else:
            key = 'fuli'
            movies = get_bt(key)
    t = loader.get_template('index.html')
    content = []
    content.append(movies)
    content.append(key)
    c = Context({'content': content})
    return HttpResponse(t.render(c))

