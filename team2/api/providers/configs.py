import inject

from django.core.cache import cache
from api.products.repositories import *
from api.products.usecases import *
from team2.infrastructure import Cache

def api_providers_config(binder: inject.Binder):
    from django_redis import get_redis_connection
    binder.bind(RepositoryInterface, ProductRepository(inject.attr(Cache)))

    binder.bind(UsecaseInterface, ProductUsecase())
