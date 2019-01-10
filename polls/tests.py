from django.test import TestCase
import datetime
from django.utils import timezone
from django.urls import reverse
from .models import Question


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)


class QuestionIndexViewTests(TestCase):
    def test_no_question(self):
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, 'No polls are available.')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_has_question(self):
        create_question('whats up?', 1)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest_question_list'],
                                 ['<Question: whats up?>'])


class QuestionDetailView(TestCase):
    def test_feature_question(self):
        feature_question = create_question('whats up?', 5)
        response = self.client.get(
            reverse('polls:detail', args=(feature_question.id, )))
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question('whats up?', -5)
        response = self.client.get(
            reverse('polls:detail', args=(past_question.id, )))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, past_question.question_text)


class QuestionCreateAndUpdateView(TestCase):
    def test_create_question(self):
        question = self.client.post(
            reverse('polls:create'), {
                'question_text': "whats up?",
                'pub_date': '2018-5-4'
            })
        self.assertEqual(Question.objects.last().question_text, 'whats up?')

    def test_update_question(self):
        question = create_question('whats up?', -5)
        response = self.client.post(
            reverse('polls:update', args=(question.id, )),
            {'question_text': "whats new?"})
        question.refresh_from_db()
        self.assertEqual(question.question_text, 'whats new?')
        self.assertRedirects(response, reverse('polls:index'))
