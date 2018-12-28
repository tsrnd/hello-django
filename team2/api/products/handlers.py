"""This module does blah blah"""
import json

from django.views import View
from django.http import HttpResponse

from api.serializers.product_serializer import ProductSerializer

class ProductsHandler(View):
    """This class processing about list of products blah blah"""

    view_factory = None

    def get(self, request, *args, **kwargs):
        products = self.view_factory.create().get_products()

        return HttpResponse(json.dumps(ProductSerializer.serializes(products)), status=200, content_type='application/json')

class ProductHandler(View):
    """This class processing about a product"""

    view_factory = None
    def get(self, request, id):
        product, status = self.view_factory.create().get_product(id)
        if status != 200:
            return HttpResponse(json.dumps({"message": "Can't get product"}), status=status, content_type='application/json')
        return HttpResponse(json.dumps(ProductSerializer.serialize(product)), status=200, content_type='application/json')
