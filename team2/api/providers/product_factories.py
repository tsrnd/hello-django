"""This module does blah blah"""

from django.core.cache import cache

from api.products.repositories import ProductRepository
from api.products.usecases import ProductUsecase

class ProductRepoFactory:
    """This class does blah blah"""
    @staticmethod
    def get():
        from django_redis import get_redis_connection
        return ProductRepository(get_redis_connection("default"))

class ProductUsecaseFactory:
    """This class does blah blah"""
    @staticmethod
    def create():
        product_repo = ProductRepoFactory.get()
        return ProductUsecase(product_repo)
