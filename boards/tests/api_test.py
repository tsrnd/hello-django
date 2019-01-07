from django.urls import reverse, resolve
from django.test import TestCase
from ..views import home
from boards.models import Board
import pytest


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        assert response.status_code == 200

    def test_home_url_resolves_home_view(self):
        view = resolve('/demo/')
        self.assertEqual(view.func, home)

class BoardTopicTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django Board')

    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'id_board': 2})
        response = self.client.get(url)
        assert response.status_code == 200

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'id_board': 99})
        response = self.client.get(url)
        assert response.status_code == 404

    # def test_board_topics_url_resolves_board_topics_view(self):
    #     view = resolve('/boards/1/')
    #     self.assertEquals(view.func, board_topics)
