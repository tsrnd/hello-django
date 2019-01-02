import pytest
from django.test import SimpleTestCase
from django.urls import reverse

def fibonacci(n, a=0, b=1):
	if n == 0: # edge case
		return a
	if n == 1: # usual base case
		return b
	return fibonacci(n-1, b, a+b)

class HomePageTests(SimpleTestCase):

    def test_fib_10(self):
        assert(fibonacci(10) == 55)

    def test_fib_not_20(self):
        assert(fibonacci(20) != 20)	