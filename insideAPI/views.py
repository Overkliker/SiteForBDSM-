from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def add(request, table):
    return render(request, 'add_shop.html')


def change(request, table, id):
    return render(request, 'change_product.html')


def delete(request, table, id):
    return render(request, 'delete_shop.html')


def check(request):
    return render(request, 'check_shops.html')