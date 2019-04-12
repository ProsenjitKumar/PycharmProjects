from django.conf.urls import re_path
from .views import (
    UserAccountSignupView,
    SuccessView,
)


urlpatterns = [
    re_path('signup/', UserAccountSignupView.as_view(), name='account_signup'),
    re_path('success/', SuccessView.as_view(), name='success'),
]