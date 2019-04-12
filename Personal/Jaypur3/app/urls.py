from django.conf.urls import re_path
from . import views


urlpatterns = [
    re_path('^$', views.home, name='home'),
    re_path('listing/', views.listing, name='listing'),
    re_path('details/', views.details, name='details'),
    re_path('map/', views.map, name='map'),
    re_path('map1/', views.map1, name='map1'),
]