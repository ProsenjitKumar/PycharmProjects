from django import forms
from .models import UserAccount


class UserAccountSignupForms(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['first_name', 'last_name', 'email', 'address', 'house_address', 'password']
