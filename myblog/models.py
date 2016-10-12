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

admin.site.register(Magic, MagicAdmin)