"""This module does blah blah"""
import json
import inject

from django.views import View
from django.http import HttpResponse

from api.serializers.product_serializer import ProductSerializer
from api.products.usecases import *

# from api.providers.configs import api_providers_config

# inject.configure_once(api_providers_config)

class ProductsHandler(View):
    """This class processing about list of products blah blah"""

    usecase: UsecaseInterface = inject.attr(ProductUsecase)

    def get(self, request, *args, **kwargs):
        products = self.usecase.get_products()

        return HttpResponse(json.dumps(ProductSerializer.serializes(products)), status=200, content_type='application/json')

class ProductHandler(View):
    """This class processing about a product"""

    usecase: UsecaseInterface = inject.attr(ProductUsecase)
    def get(self, request, id):
        product, status = self.usecase.get_product(id)
        if status != 200:
            return HttpResponse(json.dumps({"message": "Can't get product"}), status=status, content_type='application/json')
        return HttpResponse(json.dumps(ProductSerializer.serialize(product)), status=200, content_type='application/json')
