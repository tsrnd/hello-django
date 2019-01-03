"""This module use to blab blab"""
from django.urls import re_path
from api.products.handlers import ProductHandler, ProductsHandler

urlpatterns = [
    re_path(
        r'^products/$',
        ProductsHandler.as_view(),
        name='get-all-products',
    ),
    re_path(
        r'^products/(?P<id>\d+)$',
        ProductHandler.as_view(),
        name='get-product',
    ),
]
