from django.conf.urls import url
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from employees import views


urlpatterns = [
    path('employees/', views.ListEmployeeView.as_view(), name='employee-list')
]
