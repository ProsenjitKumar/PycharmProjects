from django.conf.urls import re_path
from .views import HomeView


urlpatterns = [
    re_path('^$', HomeView.as_view(), name='home'),
]