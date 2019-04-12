from django.contrib.gis import admin
from .models import WorldBorder, Market, PoliceStation
#from django.contrib import admin

#admin.site.register(WorldBorder, admin.GeoModelAdmin)


# class WorldBorderAdmin(admin.ModelAdmin):
#     list_per_page = 25
#     search_fields = ['name']
#
# admin.site.register(WorldBorderAdmin)

#admin.site.register(WorldBorder, admin.OSMGeoAdmin)
admin.site.register(WorldBorder, admin.OSMGeoAdmin)
admin.site.register(Market, admin.OSMGeoAdmin)
admin.site.register(PoliceStation, admin.OSMGeoAdmin)


