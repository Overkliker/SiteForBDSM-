from django.urls import path, re_path
from insideAPI.views import *

urlpatterns = [
    path('add/', add),
    path('change/<int:id>', change),
    path('delete/<int:id>', delete),
    path('check', check),

]
