from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.views.generic import ListView, DetailView


# Product List View
class ProductListView(ListView):
    model = Product
    template_name = 'products/products-list.html'
    paginate_by = 12
    extra_context = (
        Category.objects.all()
    )


# Product Details View
class ProductDetailsView(DetailView):
    model = Product
    template_name = 'products/products-details.html'



# function base views
'''
def sigle(request):
    return render(request, 'single.html')


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'index.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)
'''
