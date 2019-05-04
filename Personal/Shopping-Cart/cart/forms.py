from django import forms
from shop.models import Product
from orders.models import OrderItem


# current_stock = []
# for product, item in zip(Product.objects.all(), OrderItem.objects.all()):
#     if product.id == item.id:
#         current_stock.append(product.stock - item.quantity)

current_stock = []
products = Product.objects.all()
for stock in products:
    current_stock.append(stock.stock + 1)


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, current_stock[0])]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
