"""This module does blah blah."""

import json
from datetime import datetime
from api.entities.product_entities import Product
from api.serializers.product_serializer import ProductSerializer

class ProductRepository:
    """This class does blah blah."""
    def __init__(self, redis):
        self.redis = redis

    def get_product(self, _id):
        """This method does blah blah."""        
        # product = self.redis.get("product:"+_id)
        try:
            product = Product.objects.get(id=_id)
        except Product.DoesNotExist:
            return None

        im_url = self.redis.get("product_image:"+product.im_url)
        if im_url is None:
            im_url = self.generate_im_url(product.im_url)
            self.redis.set("product_image:"+product.im_url, im_url)
        else:
            im_url = im_url.decode('utf-8')

        product.im_url = im_url
            
        return product

    def get_products(self):
        """This method does blah blah."""
        products = Product.objects.all()
        return products

    def generate_im_url(self, url):
        return url+str(datetime.now())
