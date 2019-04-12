from django.shortcuts import render
from .models import Bd
from django.contrib.gis import admin



def bd(request):
    bd = Bd.objects.all()
    #bd_map = admin.site.register(admin.OSMGeoAdmin)
    context = {
        "bd": bd,
        #"bd_map": bd_map,
    }
    return render(request, 'bd/bd.html', context)