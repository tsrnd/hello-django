from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from topics import views
 
 
urlpatterns = [
    url(r'^topics/$', views.TopicList.as_view(), name='topic-list'),
    url(r'^topics/<int:pk>/$', views.TopicDetail.as_view(), name='topic-detail'),
]