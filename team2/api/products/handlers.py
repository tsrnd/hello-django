"""This module does blah blah"""
import json

from django.views import View
from django.http import HttpResponse

from api.serializers.product_serializer import ProductSerializer

class ProductHandler(View):
    """This class does blah blah"""

    view_factory = None

    def get(self, request, *args, **kwargs):
        products = self.view_factory.create().get_products()

        return HttpResponse(json.dumps(ProductSerializer.serializes(products)), status=200, content_type='application/json')
