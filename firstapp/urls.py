from django.urls import path

from . import views
# app_name = 'firstapp'
urlpatterns = [
    path('employees/index', views.index, name='index'),
    path('employee/<int:employee_id>/detail', views.detail, name='detail'),
    path('employee/create', views.create_employee, name='create_employee'),
    path(
        'employee/create_employee_submit',
        views.create_employee_submit,
        name='create_employee_submit'),
    path('employee/<int:employee_id>/edit', views.edit_employee, name='edit_employee'),
    path('employee/<int:employee_id>/edit_employee_submit', views.edit_employee_submit, name='edit_employee_submit'),
    path('employee/<int:employee_id>/delete', views.delete_employee, name='delete_employee'),
    path('employees', views.employees_list)
]
