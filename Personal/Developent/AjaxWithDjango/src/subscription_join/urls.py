from django.conf.urls import re_path
from .views import JoinFormView


urlpatterns = [
    re_path('^$', JoinFormView.as_view(), name='join'),
]