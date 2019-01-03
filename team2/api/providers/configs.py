import inject

from api.products.repositories import *
from api.products.usecases import *

def api_providers_config(binder: inject.Binder):
    product_repo = ProductRepository()
    product_usecase = ProductUsecase()
    binder.bind(RepositoryInterface, product_repo)
    binder.bind(UsecaseInterface, product_usecase)
