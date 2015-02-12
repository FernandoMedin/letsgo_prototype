from django.conf.urls import patterns, include, url
from django.contrib import admin
from lets_backend.views import LetsView

admin.autodiscover()
inst_view = LetsView()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^teste/', inst_view.name),
    url(r'^new_user/', inst_view.new_user),
)
