"""This module use to blab blab"""

from django.urls import re_path
from api.providers.product_factories import ProductUsecaseFactory
from api.products.handlers import ProductHandler

urlpatterns = [
    re_path(
        r'^products/$',
        ProductHandler.as_view(view_factory=ProductUsecaseFactory),
        name='get-all-products',
    ),
    # re_path(
    #     r'^products/a$',
    #     ProductHandler.as_view(view_factory=ProductUsecaseFactory),
    #     name='get-product',
    # ),
]
