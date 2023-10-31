from django.urls import path, re_path
from catalog.views import *

urlpatterns = [
    path('shop/<int:id>/', return_shop),
    path('shop/<int:id>/add', return_product_add),

    path('', return_catalog, name='catalog'),
    path('change/<int:id>', return_product_change, name='change'),

    path('support', return_support, name='catalog/support'),
]
