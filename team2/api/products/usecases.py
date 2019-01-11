import inject

from abc import ABCMeta, abstractmethod
from api.products.repositories import *

class UsecaseInterface(metaclass=ABCMeta):
    """ This class is usecase interface """
    @abstractmethod
    def get_products(self):
        pass
    
    @abstractmethod
    def get_product(self, _id):
        pass

class ProductUsecase(UsecaseInterface):
    repository: RepositoryInterface = inject.attr(ProductRepository)
    
    def get_products(self):
        return self.repository.get_products()

    def get_product(self, _id):
        product = self.repository.get_product(_id)
        if product is None:
            return None, 404
        return product, 200
