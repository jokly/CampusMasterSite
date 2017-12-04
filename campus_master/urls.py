from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
    url(r'^$', views.show_complaints, name='show_complaints'),
    url(r'^accounts/logout/$', logout, {'next_page': '/'}),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
