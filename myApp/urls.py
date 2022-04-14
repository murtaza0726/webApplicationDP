from django.urls import path, include
from django.contrib import admin
#from django.conf import settings
#from django.conf.urls.static import static
from myApp import views
urlpatterns = [
    path('', views.home, name="home"),
    path('group', views.group, name="group"),
    path('about', views.about, name="about"),
    path('chart', views.dome, name="dome"),
    path('graph', views.graph, name="graph"),
    #path('chart', include('project.urls')),
]