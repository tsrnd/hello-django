import inject

from django.test import TestCase
from api.entities.product_entities import Product
from api.products.repositories import RepositoryInterface, ProductRepository
from team2.infrastructure import *
from api.tests import TestException

class ProductRedisTestCaseGetError(TestCase):
    def setUp(self):
        inject.clear_and_configure(lambda binder: binder
            .bind(Cache, CacheMock("product1", "product1.jpg", "can't get", None)) \
            .bind(RepositoryInterface, ProductRepository()))
        Product.objects.create(name="Product1", category=1, im_url="product1.jpg")
        Product.objects.create(name="Product2", category=1, im_url="product2.jpg")

    def test_product_image_is_exist_on_redis_fail(self):
        with self.assertRaises(TestException):
            ProductRepository().get_product(1)
    
    def tearDown(self):
        inject.clear()
