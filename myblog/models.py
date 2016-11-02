from django.db import models
from django.contrib import admin


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    timestamp = models.DateTimeField()

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'timestamp')
admin.site.register(BlogPost, BlogPostAdmin)

class Magic(models.Model):
    mid = models.CharField(max_length=10)
    name = models.CharField(max_length=20)

class MagicAdmin(admin.ModelAdmin):
    list_display = ('mid', 'name')

class LoginRecord(models.Model):
    ip = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    url = models.CharField(max_length=20)
    account = models.CharField(max_length=20)

class LoginRecordAdmin(admin.ModelAdmin):
    list_display = ('ip', 'region','time','url','account')

class blog(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    timestamp = models.DateTimeField()
    view    =  models.CharField(max_length=5)
    authorid = models.CharField(max_length=10)

class user(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    nickName = models.CharField(max_length=100)
    creatTime = models.DateTimeField()
    latestLogin =  models.DateTimeField()
    status = models.CharField(max_length=1)
    iconUrl = models.CharField(max_length=100)
    iconUrl_small = models.CharField(max_length=100)


    
