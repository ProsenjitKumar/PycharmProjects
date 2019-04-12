from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.BlogIndexView.as_view(), name='blog_index'),
]