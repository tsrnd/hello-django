from django.test import TestCase
import datetime
from django.utils import timezone

from .models import Employees
from django.urls import reverse


class EmployeeModelTests(TestCase):

    def test_was_published_recently_with_future_employee(self):
        time = timezone.now() - datetime.timedelta(days=30)
        future_employee = Employees(join_date=time)
        self.assertIs(future_employee.was_published_recently(), False)

    def test_was_published_recently_with_old_employee(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_employee = Employees(join_date=time)
        self.assertIs(old_employee.was_published_recently(), False)

    def test_was_published_recently_with_recent_employee(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_employee = Employees(join_date=time)
        self.assertIs(recent_employee.was_published_recently(), True)

class EmployeeTest(TestCase):

    def create_employee(self, first_name, last_name, email, join_date):
        return Employees.objects.create(first_name=first_name, last_name=last_name, email=email, join_date=join_date)

    def test_employee_creation(self):
        w = self.create_employee(first_name="test", last_name="test", email= "test", join_date=timezone.now())
        self.assertTrue(isinstance(w, Employees))
        self.assertEqual(w.__unicode__(), (w.first_name,w.last_name))
    
    def test_employee_list_view(self):
        w = self.create_employee(first_name="test", last_name="test", email= "test", join_date=timezone.now())
        url = reverse("index")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')


    

