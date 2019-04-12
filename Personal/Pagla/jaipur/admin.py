from django.contrib.gis import admin
from .models import Restaurant


class RestaurantAdmin(admin.OSMGeoAdmin):
    list_per_page = 25
    list_filter = ['restaurant', 'type', 'cost', 'address']
    search_fields = ['restaurant', 'type', 'cost', 'address']


admin.site.register(Restaurant, RestaurantAdmin)