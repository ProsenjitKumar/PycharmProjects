from django.conf.urls import re_path
from . import views


urlpatterns = [
    re_path('bd/', views.bd, name='bd'),
]