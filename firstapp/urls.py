from django.urls import path

from . import views
# app_name = 'firstapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:employee_id>/detail', views.detail, name='detail'),
    path('create', views.create_employee, name='create_employee'),
    path(
        'create_employee_submit',
        views.create_employee_submit,
        name='create_employee_submit'),
    path('<int:employee_id>/edit', views.edit_employee, name='edit_employee'),
    path('<int:employee_id>/edit_employee_submit', views.edit_employee_submit, name='edit_employee_submit'),
    path('<int:employee_id>/delete', views.delete_employee, name='delete_employee')
]
