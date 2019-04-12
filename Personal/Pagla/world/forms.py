from django.contrib.gis import forms

class MyGeoForm(forms.MultiPolygonField):
    point = forms.PointField(widget=
        forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500}))