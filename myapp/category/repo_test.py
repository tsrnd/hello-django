from django.test import TestCase
import pytest
from myapp.category.repository import Repository
from django.core.cache import cache


class RepositoryTest(TestCase):
    def test(self):
        cates, err = Repository(cache).get_all_category()
        assert len(cates) == 0
        assert err == None
