from django.conf.urls import include, url
from django.views.generic import RedirectView
from django.contrib import admin
admin.autodiscover()

from myblog.views import archive,index,search,game,LoginRecord,ajaxTest,ajax_dict,blogIndex

urlpatterns = [
    url(r'^admin', include(admin.site.urls)),
    url(r'^blogIndex', blogIndex),
    url(r'^blog', archive),
    url(r'^game', game),
    url(r'^search', search),
    url(r'^LoginRecord', LoginRecord),
    url(r'^ajaxTest', ajaxTest),
    url(r'^ajax_dict', ajax_dict),
    url(r'^favicon\.ico$', RedirectView.as_view(url='static/favicon.ico')),
    url(r'^', index),
]
