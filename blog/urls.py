from django.conf.urls import include, url
from django.views.generic import RedirectView
from django.contrib import admin
admin.autodiscover()

from myblog.views import archive,indexpage,search,game,loginrecord,ajaxtest,ajax_dict,blogindex,bloglist,blogdetail,blogedit,saveblog,register,registerconfirm,registercheck,login,logincheck,loginconfirm,loginout,resetpassword,resetpwdconfirm

urlpatterns = [
    url(r'^admin', include(admin.site.urls)),
    url(r'^registerConfirm', registerconfirm),
    url(r'^registerCheck', registercheck),
    url(r'^register', register),
    url(r'^loginCheck', logincheck),
    url(r'^loginConfirm', loginconfirm),
    url(r'^loginOut', loginout),
    url(r'^login', login),
    url(r'^resetPassword', resetpassword),
    url(r'^resetpwdConfirm', resetpwdconfirm),
    url(r'^blogIndex', blogindex),
    url(r'^blogList', bloglist),
    url(r'^blogDetail', blogdetail),
    url(r'^blogEdit', blogedit),
    url(r'^saveBlog', saveblog),
    url(r'^blog', archive),
    url(r'^game', game),
    url(r'^search', search),
    url(r'^LoginRecord', loginrecord),
    url(r'^ajaxTest', ajaxtest),
    url(r'^ajax_dict', ajax_dict),
    url(r'^favicon\.ico$', RedirectView.as_view(url='static/favicon.ico')),
    url(r'^', indexpage),
]
