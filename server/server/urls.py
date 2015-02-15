from django.conf.urls import patterns, include, url
from django.contrib import admin
from lets_backend.views import LetsView

admin.autodiscover()
inst_view = LetsView()

urlpatterns = patterns('',
    url(r'^new_user/', inst_view.new_user),
    url(r'^login/', inst_view.login),
)
