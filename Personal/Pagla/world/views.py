from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q
from .models import WorldBorder
from django.contrib.gis import admin
from .forms import MyGeoForm


def home(request):
    countries = WorldBorder.objects.all()
    form = MyGeoForm()
    context = {
        "countries": countries,
        "form": form,
    }
    return render(request, 'home.html', context)

def list(request):
    if request.method == 'POST':
        search = request.POST['search']

        if search:
            match = WorldBorder.objects.filter(
                Q(name__startswith=search) |
                Q(area__icontains=search) |
                Q(region__startswith=search) |
                Q(lon__icontains=search) |
                Q(lat__icontains=search)
            )
            if match:
                return render(request, 'world/list.html', {"match": match})
            else:
                messages.error(request, "No result found")
        else:
            return HttpResponseRedirect('/')

    # args = {
    #     "users": User.objects.all(),
    # }
    return render(request, 'home.html')