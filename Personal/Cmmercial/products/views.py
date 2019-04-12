from django.shortcuts import render
from .models import ProductCategory, Product


def index(request):
    return render(request, 'home.html')


def home(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'index.html', context)


def product_detail(request, product_id):
    products = Product.objects.get(id=product_id)
    context = {
        'products': products,
    }
    template = 'product/product_detail.html'
    return render(request, template, context)

def charge(request):
    template = 'product/payment.html'
    return render(request, template)



