from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('test', views.SnipListView.as_view(), name='listview'),
    path('join', views.JoinListView.as_view(), name='join'),
    path('<int:pk>', views.SnippetDetail.as_view(), name='detail'),
    path('', views.SnippetList.as_view(), name='index'),
]

urlpatterns = format_suffix_patterns(urlpatterns)