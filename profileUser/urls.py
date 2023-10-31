from django.contrib import admin
from django.urls import path, re_path
from profileUser.views import *

urlpatterns = [
    path('<str:id>/', return_profile, name='profile'),
]
