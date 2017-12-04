from django.urls import path
from django.conf.urls import include
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
    path(r'', views.main, name='main'),
    path(r'complaints/', views.complaints, name='complaints'),
    path(r'export/xls/', views.export_complaints_xls, name='export_complaints_xls'),
    path(r'accounts/logout/', logout, {'next_page': '/'}),
    path(r'accounts/', include('django.contrib.auth.urls')),
]
