"""This module does blah blah"""

from django.core.cache import cache

from api.products.repositories import ProductRepository
from api.products.usecases import ProductUsecase
from api.products.handlers import ProductHandler

class ProductRepoFactory:
    """This class does blah blah"""
    @staticmethod
    def get():
        return ProductRepository(cache)

class ProductUsecaseFactory:
    """This class does blah blah"""
    @staticmethod
    def create():
        product_repo = ProductRepoFactory.get()
        return ProductUsecase(product_repo)
