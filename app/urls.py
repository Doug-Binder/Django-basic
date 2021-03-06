from django.conf.urls import patterns, url
from app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name="about"),
    url(r'^location/([\w-]+)/$', views.LocationView.as_view())
    )