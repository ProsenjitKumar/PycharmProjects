from django.conf.urls import url, re_path
from . import views

app_name = 'shop'

urlpatterns = [
    re_path(r'^single/', views.single, name='single'),
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^product-id=(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]
