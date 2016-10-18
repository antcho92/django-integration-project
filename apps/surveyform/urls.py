from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^survey/process$', views.process),
    url(r'^survey/results$', views.results),
    url(r'^goback$', views.goback),
]
