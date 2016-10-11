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