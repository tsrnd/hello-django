from django.shortcuts import render
from rest_framework import generics
from .models import Employees
from .serializers import EmployeesSerializer
# Create your views here.


class ListEmployeeView(generics.ListAPIView):
    """
    Provide a get method handler
    """
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
