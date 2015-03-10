from clinic import views
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^clinic/', include('clinic.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^login/$', 'django.contrib.auth.views.login', {
        'template_name': 'clinic/login.html'
    }, name='login'),
    
    url(r'^logout/$', 'django.contrib.auth.views.logout', {
        'next_page': 'index'
    }, name='logout'),
    
    url(r'^register/$', views.register, name='register'),
)
