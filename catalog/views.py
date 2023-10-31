from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def return_shop(request, id):
    data = {'id': id}
    return render(request, 'shop.html', data)


def return_product_add(request, id):
    data = {'id': id}
    return render(request, 'add_product.html', data)


def return_catalog(request):
    return render(request, 'catalog.html')


def return_product_change(request, id):
    data = {'id': id}
    return render(request, 'change_product.html', data)


def return_support(request):

    return render(request, 'support.html')