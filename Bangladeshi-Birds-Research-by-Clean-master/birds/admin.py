from django.contrib.gis import admin
from .models import (
    Birds, Kingdom, Phylum, Class, Order,
)


class BirdsAdmin(admin.ModelAdmin):
    list_display = ['kingdom', 'scientific_name', 'year']
    list_filter = ['kingdom', 'scientific_name', 'year']
    list_per_page = 50
    search_fields = ['kingdom', 'scientific_name', 'year']
    prepopulated_fields = {'slug':('kingdom',)}


admin.site.register(Birds, BirdsAdmin)


class KingdomAdmin(admin.ModelAdmin):
    list_display = ['kingdom']
    search_fields = ['kingdom']
    list_filter = ['kingdom']
    list_per_page = 50
    prepopulated_fields = {'slug':('kingdom',)}


admin.site.register(Kingdom, KingdomAdmin)


class PhylumAdmin(admin.ModelAdmin):
    list_display = ['phylum', 'kingdom']
    search_fields = ['phylum']
    list_filter = ['phylum']
    list_per_page = 50
    prepopulated_fields = {'slug':('phylum',)}


admin.site.register(Phylum, PhylumAdmin)


class ClassAdmin(admin.ModelAdmin):
    list_display = ['birds_class']
    search_fields = ['birds_class']
    list_filter = ['birds_class']
    list_per_page = 50
    prepopulated_fields = {'slug':('birds_class',)}


admin.site.register(Class, ClassAdmin)