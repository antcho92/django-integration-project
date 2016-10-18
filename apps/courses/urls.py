from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add_course, name='add'),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name='destroy'),
    url(r'^confirm/(?P<id>\d+)$', views.confirm_destroy, name='confirm_destroy')
]
