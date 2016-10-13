from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

from myblog.views import archive,index,search,game

urlpatterns = [
    url(r'^admin', include(admin.site.urls)),
    url(r'^blog', archive),
    url(r'^game', game),
    url(r'^search', search),
    url(r'^', index),

]
