from django import forms


class JoinForm(forms.Form):
	name = forms.CharField(max_length=255)
	email = forms.EmailField()

