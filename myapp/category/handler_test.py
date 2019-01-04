from django.test import TestCase
import pytest
import requests
from myapp.category.handler import Handler
from django.http import HttpRequest, QueryDict


class HandlerTest(TestCase):
    req_get = HttpRequest()
    req_post = HttpRequest()
    req_post.method = 'POST'
    req_post.POST = QueryDict('name=sss')

    def test_get_success(self):
        resp = Handler(
            view_factory=MockUseCase(mock_dict={
                'get_all_category_result': [],
                'get_all_category_err': None
            })).get(request=self.req_get)
        assert resp.status_code == 200

    def test_get_fail(self):
        resp = Handler(
            view_factory=MockUseCase(
                mock_dict={
                    'get_all_category_result': [],
                    'get_all_category_err': "get category err",
                })).get(request=self.req_get)
        assert resp.status_code == 500

    def test_post_success(self):
        resp = Handler(
            view_factory=MockUseCase(mock_dict={'create_err': None})).post(
                request=self.req_post)
        assert resp.status_code == 200

    def test_post_fail(self):
        resp = Handler(
            view_factory=MockUseCase(
                mock_dict={'create_err': "create err"})).post(
                    request=self.req_post)
        assert resp.status_code == 500


class MockUseCase():
    def __init__(self, mock_dict):
        self.mock_dict = mock_dict

    def get_all_category(self):
        return self.mock_dict['get_all_category_result'], self.mock_dict[
            'get_all_category_err']

    def create(self, name):
        return self.mock_dict['create_err']
