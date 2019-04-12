from django.contrib.gis import admin
from .models import Bd, Hospital2


class BdAdmin(admin.OSMGeoAdmin):
    list_per_page = 25
    list_filter = ['name']
    search_fields = ['name']
    # default_lat = 23
    # default_lon = 89
    # # default_zoom = 15
    # # readonly_fields = ('latitude', 'longitude')


admin.site.register(Bd, BdAdmin)

class HospitalAdmin(admin.OSMGeoAdmin):
    list_per_page = 25
    list_filter = ['hospital_n']
    search_fields = ['hospital_n']
    # default_lat = 23
    # default_lon = 89
    # # default_zoom = 15
    # # readonly_fields = ('latitude', 'longitude')


admin.site.register(Hospital2, HospitalAdmin)
