from django.test import TestCase
import pytest
import requests
from django.http import HttpRequest, QueryDict
from unittest.mock import patch
from myapp1.question_choice.views import index
from myapp1.question_choice.models import Question


class Views_Test(TestCase):
    @patch("myapp1.question_choice.models.Question.objects.order_by")
    def test_index(self, mock_get_question):
        mock_get_question.return_value = []
        response = index(HttpRequest())
        html = response.content.decode('utf8')
        self.assertIn('<p>No polls are available.</p>', html)
