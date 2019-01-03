import inject

from abc import ABCMeta, abstractmethod


class Cache(metaclass=ABCMeta):
    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def set(self, key, value):
        pass


class CacheMock(Cache):
    pass


def cache(binder: inject.Binder):
    from django_redis import get_redis_connection
    redis = get_redis_connection("default")
    binder.bind(Cache, redis)
