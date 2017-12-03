from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.show_complaints, name='show_complaints'),
]