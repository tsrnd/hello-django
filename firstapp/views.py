from django.shortcuts import render
from django.http import HttpResponse
from .models import Employees
from django import template
from django.template.loader import get_template

# Create your views here.


def index(request):
    employee_list = Employees.objects.order_by('-id')
    template = get_template('index.html')
    context = {
        'employee_list': employee_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, employee_id):
    return HttpResponse("You're employee %s." % employee_id)
