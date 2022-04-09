from django.urls import re_path,path
from . import views
from django.contrib.auth import views as auth_views
from .views import ListProfileView, ListProjectView

urlpatterns=[
    # re_path('^$',views.welcome,name = 'welcome'),
    path('',views.home,name = 'home'),
    path('project/<project_id>/',views.project,name ='project'),
    path('search/', views.search_results, name='search_results'),
    path('profile/', views.profile, name='profile'),
    path('update/', views.update, name='update'),
    path('upload_project/', views.upload_project, name='upload_project'),
]