from django.test import TestCase
import pytest
from django.urls import reverse


class API_Test(TestCase):
    def test_api_index(self):
        response = self.client.get(reverse('myapp1:index'))
        assert response.status_code == 200
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
