from django.conf.urls import re_path
from .views import (
    ProductListView, ProductDetailsView
)

# app_name = 'products'

urlpatterns = [
    re_path('^$', ProductListView.as_view(), name='product_list'),
    re_path('(?P<slug>[-\w]+)/product-id=(?P<id>\d+)/$', ProductDetailsView.as_view(), name='product_details')
]
#
# app_name = 'shop'
#
# urlpatterns = [
#     re_path(r'^single/', views.sigle, name='single'),
#     url(r'^$', views.product_list, name='product_list'),
#     url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
#     url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
# ]
