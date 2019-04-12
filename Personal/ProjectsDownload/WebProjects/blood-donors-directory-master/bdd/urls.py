from django.conf.urls import url

from . import apis

urlpatterns = [
    url(r'api/blood-group/$', apis.BloodGroupAPIView.as_view()),
    url(r'api/blood-group/(?P<pk>[0-9a-z\-]+)/$', apis.BloodGroupAPIView.as_view()),
    url(r'api/donor/$', apis.DonorAPIView.as_view()),
    url(r'api/donor/(?P<pk>[0-9a-z\-]+)/$', apis.DonorAPIView.as_view()),
    url(r'api/register/$', apis.RegisterAPIView.as_view()),
    url(r'api/register/(?P<pk>[0-9a-z\-]+)/$', apis.RegisterAPIView.as_view()),
]
