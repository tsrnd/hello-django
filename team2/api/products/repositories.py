"""This module does blah blah."""
from api.entities.product_entities import Product

class ProductRepository:
    """This class does blah blah."""
    def __init__(self, redis):
        self.redis = redis 
    def get_product(self, _id):
        """This method does blah blah."""        
        product = self.redis.get("product:"+_id)

        if product is None:
            product = Product.objects.get(id=_id)
        return product

    def get_products(self):
        """This method does blah blah."""       
        products = Product.objects.all()
        return products
