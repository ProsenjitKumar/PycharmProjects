from django.conf.urls import re_path
from . import views

urlpatterns = [
    re_path('index/', views.index, name='index'),
    re_path('^$', views.home, name='home'),
    re_path(r'^product-detail/(?P<product_id>[0-9]+)/$', views.product_detail, name='product-detail'),
    re_path(r'^charge/$', views.charge, name='charge'),
]