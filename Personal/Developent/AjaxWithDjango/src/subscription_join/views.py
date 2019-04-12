from django.shortcuts import render
from .forms import JoinForm
from django.views.generic import FormView


class JoinFormView(FormView):
	"""docstring for JoinFormView"""
	form_class = JoinForm
	template_name = 'ajax.html'
	success_url = 'Thanks'

