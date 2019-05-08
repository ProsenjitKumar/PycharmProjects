from django import forms
from .models import Organization
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# class OrganizationForm(forms.ModelForm):
#     class Meta:
#         model = Organization
#         fields = ('org_name', 'org_short_name', 'address', 'telephone', 'whatsapp', 'fax', 'p_o_box', 'permit_number',
#                     'permit_date', 'board_members', 'info', 'org_types', 'goals', 'projects', 'state', 'city',
#                   'org_links')


class RegisterForm(UserCreationForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    org_name = forms.CharField(max_length=200)
    org_short_name = forms.CharField(max_length=200)
    logo = forms.ImageField(required=False)
    address = forms.CharField(max_length=260)
    telephone = forms.IntegerField()
    whatsapp = forms.IntegerField()
    fax = forms.CharField(max_length=50)
    p_o_box = forms.CharField(max_length=80)
    permit_number = forms.CharField(max_length=15)
    permit_date = forms.CharField(max_length=10)
    board_members = forms.CharField(max_length=1000)
    info = forms.CharField(max_length=1000)
    org_types = forms.CharField(max_length=56)
    goals = forms.CharField(max_length=1000)
    projects = forms.CharField(max_length=1000)
    # permit Issuer
    state = forms.CharField(max_length=88)
    city = forms.CharField(max_length=88)
    org_links = forms.URLField()

    class Meta:
        model = User
        fields = ('org_name', 'org_short_name', 'logo', 'address', 'telephone', 'whatsapp', 'fax', 'p_o_box', 'permit_number',
                    'permit_date', 'board_members', 'info', 'org_types', 'goals', 'projects', 'state', 'city',
                  'org_links')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.active = True # send for admin approval if user.active=False
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)