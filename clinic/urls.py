from django.conf.urls import patterns, url

from clinic import views

urlpatterns = patterns('',
    url(r'^doctors/$', views.doctors_list, name='doctors_list'),
    url(r'^services/$', views.services_list, name='services_list'),
    url(r'^doctors/(?P<doctor_id>\d+)/$', views.doctor_page, name='doctor_page'),
    url(r'^services/(?P<service_id>\d+)/$', views.service_page, name='service_page'),
)
