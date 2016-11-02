from django.conf.urls import include, url
from django.views.generic import RedirectView
from django.contrib import admin
admin.autodiscover()

from myblog.views import archive,index,search,game,LoginRecord,ajaxTest,ajax_dict,blogIndex,blogList,blogDetail,blogEdit,saveBlog,register,registerConfirm,registerCheck,login,loginCheck,loginConfirm,loginOut,resetPassword,resetpwdConfirm

urlpatterns = [
    url(r'^admin', include(admin.site.urls)),
    url(r'^registerConfirm', registerConfirm),
    url(r'^registerCheck', registerCheck),
    url(r'^register', register),
    url(r'^loginCheck', loginCheck),
    url(r'^loginConfirm', loginConfirm),
    url(r'^loginOut', loginOut),
    url(r'^login', login),
    url(r'^resetPassword', resetPassword),
    url(r'^resetpwdConfirm', resetpwdConfirm),
    url(r'^blogIndex', blogIndex),
    url(r'^blogList', blogList),
    url(r'^blogDetail', blogDetail),
    url(r'^blogEdit', blogEdit),
    url(r'^saveBlog', saveBlog),
    url(r'^blog', archive),
    url(r'^game', game),
    url(r'^search', search),
    url(r'^LoginRecord', LoginRecord),
    url(r'^ajaxTest', ajaxTest),
    url(r'^ajax_dict', ajax_dict),
    url(r'^favicon\.ico$', RedirectView.as_view(url='static/favicon.ico')),
    url(r'^', index),
]
