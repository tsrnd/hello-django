import inject
from abc import ABCMeta, abstractmethod
from datetime import datetime
from myapp.products.models import Product
from myapp.serializers.product_serializer import ProductSerializer
from myproject.infrastructure.cache import Cache


class RepositoryInterface(metaclass=ABCMeta):
    """This class is repository interface."""
    @abstractmethod
    def get_product(self, _id):
        pass

    @abstractmethod
    def get_products(self):
        pass

    @abstractmethod
    def generate_im_url(self, url):
        pass


class ProductRepository:
    """This class does blah blah."""
    redis = inject.attr(Cache)  # type: Cache

    def get_product(self, _id):
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
