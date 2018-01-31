from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout
from campus_master_site import settings
from . import views

urlpatterns = [
    path(r'', views.main, name='main'),
    path(r'bot/', views.bot, name='bot'),
    path(r'status/', views.status, name='status'),
    path(r'complaints/', views.complaints, name='complaints'),
    path(r'export/xls/', views.export_complaints_xls, name='export_complaints_xls'),
    path(r'accounts/logout/', logout, {'next_page': '/'}),
    path(r'accounts/', include('django.contrib.auth.urls')),
    path(r'ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
