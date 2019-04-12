from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from .forms import UserAccountSignupForms


class UserAccountSignupView(FormView):
    template_name = 'accounts/user_account_signup.html'
    form_class = UserAccountSignupForms
    success_url = '/success/'


class SuccessView(TemplateView):
    template_name = 'accounts/success.html'



