from django.contrib.gis import admin
from .models import SmartRestaurant, Fort, Hospital55, Market, PoliceStation


class SmartRestaurantAdmin(admin.OSMGeoAdmin):
    list_per_page = 25
    list_filter = ['restaurant', 'type', 'cost', 'address']
    search_fields = ['restaurant', 'type', 'cost', 'address']
    # default_lat = 23
    # default_lon = 89
    # # default_zoom = 15
    # # readonly_fields = ('latitude', 'longitude')


admin.site.register(SmartRestaurant, SmartRestaurantAdmin)


class FortAdmin(admin.OSMGeoAdmin):
    list_per_page = 25
    list_filter = ['title']
    search_fields = ['title', 'category', 'descriptio']
    # default_lat = 23
    # default_lon = 89
    # # default_zoom = 15
    # # readonly_fields = ('latitude', 'longitude')


admin.site.register(Fort, FortAdmin)


class Hospital5Admin(admin.OSMGeoAdmin):
    list_per_page = 25
    list_filter = ['hospital_n']
    search_fields = ['hospital_n']
    # default_lat = 23
    # default_lon = 89
    # # default_zoom = 15
    # # readonly_fields = ('latitude', 'longitude')


admin.site.register(Hospital55, Hospital5Admin)


class MarketAdmin(admin.OSMGeoAdmin):
    list_per_page = 25
    list_filter = ['market_nam']
    search_fields = ['market_nam', 'location', 'rating']
    # default_lat = 23
    # default_lon = 89
    # # default_zoom = 15
    # # readonly_fields = ('latitude', 'longitude')


admin.site.register(Market, MarketAdmin)


class PoliceStationAdmin(admin.OSMGeoAdmin):
    list_per_page = 25
    list_filter = ['police_sta']
    search_fields = ['police_sta', 'address', 'rating', 'contact_nu']
    # default_lat = 23
    # default_lon = 89
    # # default_zoom = 15
    # # readonly_fields = ('latitude', 'longitude')


admin.site.register(PoliceStation, PoliceStationAdmin)