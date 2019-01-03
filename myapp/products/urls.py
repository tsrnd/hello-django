from django.urls import path
from myapp.products.handler import ProductHandler, ProductsHandler

urlpatterns = [
    # re_path(
    #     r'^products/$',
    #     ProductsHandler.as_view(),
    #     name='get-all-products',
    # ),
    # re_path(
    #     r'^products/(?P<id>\d+)$',
    #     ProductHandler.as_view(),
    #     name='get-product',
    # ),
    path('', ProductsHandler.as_view(), name='get-all-products'),
    path('<int:id>/', ProductHandler.as_view(), name='get-product'),
]
