from django.contrib.gis import admin
from .models import Restaurant
#from django.contrib import admin

#admin.site.register(WorldBorder, admin.GeoModelAdmin)


# class WorldBorderAdmin(admin.ModelAdmin):
#     list_per_page = 25
#     search_fields = ['name']
#
# admin.site.register(WorldBorderAdmin)

#admin.site.register(WorldBorder, admin.OSMGeoAdmin)
admin.site.register(Restaurant, admin.OSMGeoAdmin)



