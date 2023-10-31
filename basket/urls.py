from django.urls import path, re_path
from basket.views import *

urlpatterns = [
    path('<str:id>', return_basket),
]
