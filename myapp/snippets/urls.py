from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('<int:pk>', views.SnippetDetail.as_view(), name='detail'),
    path('', views.SnippetList.as_view(), name='index'),
]

urlpatterns = format_suffix_patterns(urlpatterns)