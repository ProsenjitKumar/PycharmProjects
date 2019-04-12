from django.conf.urls import url
from . import views


urlpatterns = [
    url('^$', views.home, name='home'),
    url('list/', views.list, name='list'),
    url('list1/', views.list11, name='list1'),
]