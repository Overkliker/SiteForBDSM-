from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def return_profile(request, id):
    data = {'id': id}
    return render(request, 'profile.html', data)