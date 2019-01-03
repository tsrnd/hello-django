import inject
from myapp.products.repository import *
from myapp.products.usecase import *


def myapp_providers_config(binder: inject.Binder):
    binder.bind(RepositoryInterface, ProductRepository())
    binder.bind(UsecaseInterface, ProductUsecase())
