# Create your views here.
# -*- coding: utf-8 -*-
from django.template import loader, Context
from myblog.models import BlogPost, blog
from myblog.models import user as myuser
from myblog.magnet import get_bt
from django.http import JsonResponse
from myblog.db.util import getPages, getRecords, getMaxId
from myblog.db.blog import insert
from django.shortcuts import render
from myblog.db.user import register as userregister, getUserModel
from myblog.util import getTime, qiniuUpload
import base64
import time
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as mainlogin


def game():
    raise Exception


def archive():
    posts = BlogPost.objects.all()
    t = loader.get_template('archive.html')
    c = Context({'posts': posts})
    return HttpResponse(t.render(c))


def index():
    posts = None
    t = loader.get_template('index.html')
    c = Context({'posts': posts})
    return HttpResponse(t.render(c))


def search(request):
    key = request.GET.get('key')
    page = request.GET.get('page')
    content = {}
    if key is None:
        key = ''
        movies = []
    else:
        movies = get_bt(key, page)
        if not movies:
            key = 'fuli'
            movies = get_bt(key, page)
    t = loader.get_template('index.html')
    content['movies'] = movies
    content['key'] = key
    content['page'] = page
    c = Context({'content': content})
    return HttpResponse(t.render(c))


def loginrecord(request):
    content = getPages(request, 'myblog_loginrecord', '', '', 'time')
    t = loader.get_template('LoginRecord.html')
    c = Context({'content': content})
    return HttpResponse(t.render(c))


def ajaxtest():
    posts = None
    t = loader.get_template('ajaxTest.html')
    c = Context({'posts': posts})
    return HttpResponse(t.render(c))


def ajax_dict():
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)


def blogindex():
    posts = None
    t = loader.get_template('blog/blog_index.html')
    c = Context({'posts': posts})
    return HttpResponse(t.render(c))


def bloglist(request):
    content = getPages(request, 'myblog_blog', "CONCAT(SUBSTR(t.content,1,150),'...')'summary',", '', 'timestamp')
    return render(request, 'blog/blogList.html', {'content': content})


def blogdetail(request):
    content = {}
    theid = request.GET.get('id')
    record = getRecords(1, 1, 'myblog_blog', '', ''.join(['and id = ', theid]), 'timestamp')
    content['record'] = record[0]
    content['userModel'] = getUserModel(request.user.username)
    return render(request, 'blog/blogDetail.html', {'content': content})


def blogedit(request):
    content = {}
    theid = request.GET.get('id')
    if theid is not None:
        record = getRecords(1, 1, 'myblog_blog', '', ''.join(['and id = ', theid]), 'timestamp')
        content['record'] = record[0]
    return render(request, 'blog/blogEdit.html', {'content': content})


def saveblog(request):
    blogcontent = request.POST['content']
    userid = request.user.id
    title = request.POST['title']
    blog.authorid = userid
    blog.content = blogcontent
    blog.title = title
    fmt = '%Y-%m-%d %X'
    blog.timestamp = time.strftime(fmt, time.localtime())
    blog.view = 0
    theid = insert(blog)
    content = {}
    record = getRecords(1, 1, 'myblog_blog', '', ''.join(['and id = ', str(theid)]), 'timestamp')
    content['record'] = record[0]
    return render(request, 'blog/blogDetail.html', {'content': content})


def register(request):
    return render(request, 'blog/register.html', '')


def registercheck(request):
    email = request.GET.get('email')
    nickname = request.GET.get('nickName')
    checktype = request.GET.get('checkType')
    if int(checktype) == 0:
        record = getRecords(1, 1, 'myblog_user', '', ''.join(['and email = "', str(email), '"']), 'creatTime')
    else:
        record = getRecords(1, 1, 'myblog_user', '', ''.join(['and nickName = "', str(nickname), '"']), 'creatTime')
    name_dict = {'result': len(list(record))}
    return JsonResponse(name_dict)


def login(request):
    return render(request, 'blog/login.html', '')


def registerconfirm(request):
    myuser.nickName = request.POST['nickName']
    myuser.password = request.POST['inputPassword3']
    myuser.email = request.POST['inputEmail3']
    thefile = request.FILES['upload-file']
    myuser.iconUrl = qiniuUpload("".join([myuser.email, '.jpg']), thefile)
    icon_small = request.POST['icon_small'].split(',')[1]
    myuser.iconUrl_small = qiniuUpload("".join([myuser.email, '-small.jpg']), base64.decodestring(icon_small))
    myuser.status = 1
    myuser.creatTime = getTime()
    myuser.latestLogin = getTime()
    myuser.id = getMaxId('myblog_user')
    userregister(myuser)
    user = User.objects.create_user(myuser.nickName, myuser.email, myuser.password)
    user.save()
    user = authenticate(username=myuser.nickName, password=myuser.password)
    mainlogin(request, user)
    response = HttpResponseRedirect('/index/')
    return response


def indexpage(request):
    return render(request, 'blog/blog_index.html', '')


def logincheck(request):
    password = request.GET.get('inputPassword3')
    nickname = request.GET.get('nickName')
    user = authenticate(username=nickname, password=password)
    name_dict = {'result': 0}
    if user is not None:
        if user.is_active:
            name_dict = {'result': 1}
    return JsonResponse(name_dict)


def loginconfirm(request):
    password = request.POST['inputPassword3']
    nickname = request.POST['nickName']
    user = authenticate(username=nickname, password=password)
    mainlogin(request, user)
    response = HttpResponseRedirect('/index/')
    return response


def loginout(request):
    logout(request)
    response = HttpResponseRedirect('/index/')
    return response


def resetpassword(request):
    return render(request, 'blog/resetPassword.html', '')


def resetpwdconfirm(request):
    password = request.GET.get('inputPassword3')
    nickname = request.GET.get('nickName')
    newpwd = request.GET.get('newpwd')
    user = authenticate(username=nickname, password=password)
    if user is not None and user.is_active:
        user.set_password(newpwd)
        user.save()
        mainlogin(request, user)
        name_dict = {'result': 0}
    else:
        name_dict = {'result': 1}
    return JsonResponse(name_dict)
