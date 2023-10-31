from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def return_basket(request, id):
    return render(request, 'basket.html')