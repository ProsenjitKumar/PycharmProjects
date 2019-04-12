from django.shortcuts import render


def home(request):
    return render(request, 'app/index.html')

def details(request):
    return render(request, 'app/detail.html')

def listing(request):
    return render(request, 'app/listing.html')

def map(request):
    return render(request, 'app/google map.html')

def map1(request):
    return render(request, 'app/map1.html')