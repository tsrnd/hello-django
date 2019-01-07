from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
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
    # try:
    #     employee = Employees.objects.get(pk=employee_id)
    # except Employees.DoesNotExist:
    #     raise Http404("Employee does not exist")
    employee = get_object_or_404(Employees, pk=employee_id)
    return render(request, 'detail.html', {'employee': employee})


def create_employee(request):
    return render(request, 'create.html')


def create_employee_submit(request):
    first_name = request.POST['firstname']
    last_name = request.POST['lastname']
    email = request.POST['email']
    employee_info = Employees(
        first_name=first_name, last_name=last_name, email=email
    )
    employee_info.save()
    return redirect('index')
