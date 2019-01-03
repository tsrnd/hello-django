import inject

from abc import ABCMeta, abstractmethod
from api.tests import TestException

class Cache(metaclass=ABCMeta):

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def set(self, key, value):
        pass

class CacheMock(Cache):
    
    def __init__(self, key, value, get_exception, set_exception):
        self.key = key
        self.value = value
        self.get_exception = get_exception
        self.set_exception = set_exception
    
    def get(self, key):
        if self.get_exception != None:
            raise TestException(self.get_exception)
        if self.key == key:
            return self.value
        else:
            return None

    def set(self, key, value):
        if self.set_exception != None:
            raise TestException(self.set_exception)
        self.key = key
        self.value = value

def cache(binder: inject.Binder):
    from django_redis import get_redis_connection
    redisC = get_redis_connection("default")
    binder.bind(Cache, redisC)