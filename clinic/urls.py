from django.conf.urls import patterns, url

from clinic import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^doctors/(?P<doctor_id>\d+)/$', views.doctor_page, name='doctor_page'),
    url(r'^services/(?P<service_id>\d+)/$', views.service_page, name='service_page'),
    
)
