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
    page = request.GET.get('page')
    content = {}
    if key == None:
        key = ''
        movies = []
    else:
        try:
            movies = get_bt(key,page)
            if movies:
                print 1
            else:
                key = 'fuli'
                movies = get_bt(key,page)
        except Exception, ex:
            print 1
    t = loader.get_template('index.html')
    content['movies'] = movies
    content['key'] = key
    content['page'] = page
    c = Context({'content': content})
    return HttpResponse(t.render(c))

