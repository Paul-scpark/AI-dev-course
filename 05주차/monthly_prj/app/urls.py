from django.urls import path, re_path
from app import views

urlpatterns = [
    re_path(r'^.*\.html', views.project_html, name='project'),
    re_path(r'^.*\.html', views.get_data, name='data'),
    re_path(r'^.*\.html', views.get_data_eda, name='data_eda'),
    re_path(r'^.*\.html', views.get_data_search, name='data_search'),
    re_path(r'^.*\.html', views.get_community, name='community'),
    path('', views.index, name='index'),
]
