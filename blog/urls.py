from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

from myblog.views import archive

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', archive),
]
