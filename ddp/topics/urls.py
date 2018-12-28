from django.conf.urls import url
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from topics import views
 
 
urlpatterns = [
    path('topics/', views.TopicList.as_view(), name='topic-list'),
    path('topics/<int:id>', views.TopicDetail.as_view(), name='topic-detail'),
]