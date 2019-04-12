from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, widget=forms.TextInput({
                               'class': 'form-control',
                               'placeholder': 'Name'
                          }))
    email = forms.EmailField(widget=forms.TextInput({
                               'class': 'form-control',
                               'placeholder': 'Email'
                          }))
    to = forms.EmailField(widget=forms.TextInput({
                               'class': 'form-control',
                               'placeholder': 'To'
                          }))
    comments = forms.CharField(required=False, widget=forms.Textarea({
                                'class': 'form-control',
                                'placeholder': 'Comments'
                                }))
                        

class CommentForm(forms.ModelForm):
    name = forms.CharField(max_length=255, widget=forms.TextInput({
                               'class': 'form-control',
                               'placeholder': 'Name'
                          }))
                          
    email = forms.EmailField(widget=forms.TextInput({
                               'class': 'form-control',
                               'placeholder': 'Email'
                          }))
    body = forms.CharField(required=False, widget=forms.Textarea({
                                'class': 'form-control',
                                'placeholder': 'Body'
                                }))

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class SearchForm(forms.Form):
    query = forms.CharField(widget=forms.TextInput({
                               'class': 'form-control',
                               'placeholder': 'Search Here ...'
                          }))
