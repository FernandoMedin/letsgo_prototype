from django.conf.urls import patterns, include, url
from django.contrib import admin
from lets_backend.views import LetsView

admin.autodiscover()
inst_view = LetsView()

urlpatterns = patterns('',
    url(r'^new_user/', inst_view.new_user),
    url(r'^login/', inst_view.login),
    url(r'^new_event/', inst_view.new_event),
    url(r'^get_type/', inst_view.get_event_type),
    url(r'^get_events/', inst_view.show_events),
    url(r'^get_event_data/', inst_view.test),
)
