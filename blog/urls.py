from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

from myblog.views import archive,index,search

urlpatterns = [
    url(r'^admin', include(admin.site.urls)),
    url(r'^blog', archive),
    url(r'^index', index),
    url(r'^', search),

]
