from django.conf.urls import patterns, url

from clinic import views

urlpatterns = patterns('',
    url(r'^doctors/$', views.doctors_list, name='doctors_list'),
    url(r'^$', views.index, name='index'),
    url(r'^services/$', views.services_list, name='services_list'),
    url(r'^doctors/(?P<doctor_id>\d+)/$', views.doctor_page, name='doctor_page'),
    url(r'^services/(?P<service_id>\d+)/$', views.service_page, name='service_page'),
    url(r'^appointment/(?P<service_id>\d+)/$', views.make_appointment, name='make_appointment'),
    url(r'^leave_comment/(?P<service_id>\d+)/$', views.leave_comment, name='leave_comment'),
)
