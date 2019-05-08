from django.conf.urls import re_path
from . import views


urlpatterns = [
    re_path('^$', views.home, name='home'),
    re_path('organization-user-register/', views.register_page, name='register'),
]
