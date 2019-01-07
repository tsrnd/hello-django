from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:employee_id>/detail', views.detail, name='detail'),
    path('create', views.create_employee, name='create_employee'),
    path(
        'create_employee_submit',
        views.create_employee_submit,
        name='create_employee_submit'),
]
