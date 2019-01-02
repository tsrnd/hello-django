import inject

from django.core.cache import cache
from api.products.repositories import *
from api.products.usecases import *

def api_providers_config(binder: inject.Binder):
    from django_redis import get_redis_connection
    binder.bind(RepositoryInterface, ProductRepository(get_redis_connection("default")))

    binder.bind(UsecaseInterface, ProductUsecase())
