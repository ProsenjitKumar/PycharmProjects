from django.contrib.gis import forms
from .models import SmartRestaurant

class RestaurantForm(forms.ModelForm):

    class Meta:
        model = SmartRestaurant
        fields = ['point']