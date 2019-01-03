import inject

from django.test import TestCase
from myapp.products.models import Product
from myapp.products.repository import RepositoryInterface, ProductRepository
from myproject.infrastructure.cache import *
from myproject.shared.test import CommonException


class ProductRedisTestCaseGetError(TestCase):
    def setUp(self):
        inject.clear_and_configure(lambda binder: binder.bind(
                Cache,
                CacheMock("product1", "product1.jpg", "can't get", None),
            ).bind(RepositoryInterface, ProductRepository()))
        Product.objects.create(name="Product1", category=1, im_url="1.jpg")
        Product.objects.create(name="Product2", category=1, im_url="2.jpg")

    def test_product_image_is_exist_on_redis_fail(self):
        with self.assertRaises(CommonException):
            ProductRepository().get_product(1)

    def tearDown(self):
        inject.clear()


class ProductRedisTestCaseGetFromRedisSuccess(TestCase):
    def setUp(self):
        inject.clear_and_configure(lambda binder: binder.bind(
                Cache,
                CacheMock(
                    "product_image:1.jpg",
                    bytes("product1.jpg", "utf-8"),
                    None,
                    None,
                ),
            ).bind(RepositoryInterface, ProductRepository()))
        Product.objects.create(name="Product1", category=1, im_url="1.jpg")
        Product.objects.create(name="Product2", category=1, im_url="2.jpg")
        print(Product.objects.all())

    def test_product_image_is_exist_on_redis(self):
        product = ProductRepository().get_product(3)
        self.assertEqual("product1.jpg", product.im_url)

    def tearDown(self):
        inject.clear()
