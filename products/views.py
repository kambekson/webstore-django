from django.shortcuts import render
from products.models import ProductCategory, Product


def index(request):
    context = {
        'title': 'WebStore',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'WebStore - Product',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)