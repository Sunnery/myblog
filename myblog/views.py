# Create your views here.
# -*- coding: utf-8 -*-
import math
from django.template import loader,Context
from django.http import HttpResponse
from myblog.models import BlogPost
from myblog.magnet import get_bt
from myblog.db.user import getReqLog,getReqLogTotalNum
from django.http import JsonResponse

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
            if not movies:
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

def LoginRecord(request):
    pageNum = int(15)
    page = request.GET.get('page')
    content = {}
    if page == None:
        page = 1
    page = int(page)
    LoginRecords = getReqLog(page,pageNum)
    totalNum = getReqLogTotalNum()
    pages = []
    totalPages = math.ceil(float(totalNum)/pageNum)
    start = (page-4)>0 and (page-4) or 1
    end = page+4
    if end >totalPages:
        end = int(totalPages)
        start = int(totalPages - 9)
    if (end - start)<8:
        end = end + (9-end)
    for i in range(start ,end+1):
        pages.append(i)
    t = loader.get_template('LoginRecord.html')
    content['page'] = page
    content['LoginRecords'] = LoginRecords
    content['totalPages'] = int(totalPages)
    content['pages'] = pages
    c = Context({'content': content})
    return HttpResponse(t.render(c))

def ajaxTest(request):
    posts = None
    t = loader.get_template('ajaxTest.html')
    c = Context({'posts': posts})
    return HttpResponse(t.render(c))

def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)

def blogIndex(request):
    posts = None
    t = loader.get_template('blog_index.html')
    c = Context({'posts': posts})
    return HttpResponse(t.render(c))