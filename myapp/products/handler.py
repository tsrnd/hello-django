import json
import inject

from django.views import View
from django.http import HttpResponse

from myapp.serializers.product_serializer import ProductSerializer
from myapp.products.usecase import *


class ProductsHandler(View):
    """This class processing about list of products blah blah"""

    usecase = inject.attr(ProductUsecase)  # type: UsecaseInterface

    def get(self, request, *args, **kwargs):
        products = self.usecase.get_products()

        return HttpResponse(
            json.dumps(ProductSerializer.serializes(products)),
            status=200,
            content_type='application/json',
        )


class ProductHandler(View):
    """This class processing about a product"""
    usecase = inject.attr(ProductUsecase)  # type: UsecaseInterface

    def get(self, request, id):
        product, status = self.usecase.get_product(id)
        if status != 200:
            return HttpResponse(
                json.dumps({"message": "Can't get product"}),
                status=status,
                content_type='application/json',
            )
        return HttpResponse(
            json.dumps(ProductSerializer.serialize(product)),
            status=200,
            content_type='application/json',
        )
