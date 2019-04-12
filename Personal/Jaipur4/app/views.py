from urllib.error import URLError

#import geolocator as geolocator
from django.contrib.gis import geos
from django.contrib.gis import measure
from django.shortcuts import render
from geopy.geocoders.googlev3 import Geocoder
from geopy.geocoders.googlev3 import GeocoderQueryError
from  .forms import AddressForm
from .models import Shop
#from geolocator import DummyLocator

def geocode_address(address):
    address = address.encode('utf-8')
    geocoder = Geocoder()
    try:
        _, latlon = geocoder.geocode(address)
    except (BaseException, URLError, GeocoderQueryError, ValueError):
        return None
    else:
        return latlon

def get_shops(longitude, latitude):
    current_point = geos.fromstr("POINT(%s %s)" % (longitude, latitude))
    distance_from_point = {'km': 10}
    shops = Shop.gis.filter(location__distance_lte=(current_point, measure.D(**distance_from_point)))
    shops = shops.distance(current_point).order_by('distance')
    return shops.distance(current_point)

def home(request):
    form = AddressForm()
    shops = []
    if request.POST:
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            location = geocode_address(address)
            if location:
                latitude, longitude = location
                shops = get_shops(longitude, latitude)


    return render(request, 'home.html', {'form': form, 'shops': shops})