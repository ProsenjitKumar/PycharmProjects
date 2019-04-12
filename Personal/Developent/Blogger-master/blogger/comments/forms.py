from django import forms

class Commentform(forms.Form):
	content_type = forms.CharField(widget=forms.HiddenInput)
	object_id = forms.IntegerField(widget=forms.HiddenInput)
	#parent_id = forms.InputField(widget=forms.HiddenInput, required=False)
	content = forms.CharField(label='', widget=forms.Textarea)