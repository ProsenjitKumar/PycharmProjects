from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.db.models import Q
from .models import *
from bd.models import Hospital2
from django.contrib.gis import admin
from .forms import RestaurantForm


# def home(request):
#     map_info = SmartRestaurant.objects.all()
#
#     context = {
#         "map_detail": map_info
#     }
#
#     return render(request, 'home1.html', context)


def home(request):
    restaurants = SmartRestaurant.objects.all()
    context = {
        "restaurants": restaurants,
    }
    return render(request, 'home.html', context)


def list(request):
    if request.method == 'POST':
        search = request.POST['search']

        if search:
            match1 = SmartRestaurant.objects.filter(
                Q(restaurant__startswith=search) |
                Q(rating__icontains=search) |
                Q(type__startswith=search) |
                Q(features__icontains=search)
            )
            if match1:
                return render(request, 'home1.html', {"match1": match1})

            hospital = Hospital2.objects.filter(
                Q(hospital_n__startswith=search) |
                Q(hospital_r__icontains=search) |
                Q(contact_nu__startswith=search) |
                Q(address__icontains=search)
            )
            if hospital:
                return render(request, 'hospital.html', {"hospital": hospital})

            market = Market.objects.filter(
                Q(market_nam__startswith=search) |
                Q(rating__icontains=search) |
                Q(location__startswith=search) |
                Q(longitude__icontains=search)
            )
            if market:
                return render(request, 'market.html', {"market": market})

            police = PoliceStation.objects.filter(
                Q(police_sta__icontains=search) |
                Q(rating__icontains=search) |
                Q(contact_nu__startswith=search) |
                Q(latitude__icontains=search)
            )
            if police:
                return render(request, 'police.html', {"police": police})

            match = Fort.objects.filter(
                Q(title__startswith=search) |
                Q(rating__icontains=search) |
                Q(category__startswith=search) |
                Q(descriptio__icontains=search)
            )
            if match:
                return render(request, 'list.html', {"match": match})
            else:
                return HttpResponse("No result Found")
        else:
            return HttpResponseRedirect('/')

    args = {
        "users": Fort.objects.all(),
    }
    return render(request, 'home.html', args)


def list11(request):
    query = request.GET.get("q")
    if query:
        quesryset_lists = SmartRestaurant.objects.filter(restaurant__startswith=query)

        context = {
        "lists": quesryset_lists,
        }
        return render(request, 'home1.html', context)




# from django.views.generic import TemplateView
#
# class MultipleModelView(TemplateView):
#     template_name = 'template.html'
#
#     def get_context_data(self, **kwargs):
#          context = super(MultipleModelView, self).get_context_data(**kwargs)
#          context['modelone'] = ModelOne.objects.get(*query logic*)
#          context['modeltwo'] = ModelTwo.objects.get(*query logic*)
#          return context



