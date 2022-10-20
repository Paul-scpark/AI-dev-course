from django.urls import path, re_path
from app import views

urlpatterns = [
    re_path(r'^.*\.html', views.project_html, name='project'),
    path('', views.index, name='index'),
]
