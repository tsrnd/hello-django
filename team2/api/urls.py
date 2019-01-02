"""This module use to blab blab"""

from django.urls import re_path, path, include
from api.providers.product_factories import ProductUsecaseFactory
from api.products.handlers import ProductHandler, ProductsHandler

urlpatterns = [
    re_path(
        r'^products/$',
        ProductsHandler.as_view(view_factory=ProductUsecaseFactory),
        name='get-all-products',
    ),
    re_path(
        r'^products/(?P<id>\d+)$',
        ProductHandler.as_view(view_factory=ProductUsecaseFactory),
        name='get-product',
    ),
    path('test', include('test.urls')),
    # path('admin/', admin.site.urls),
]
