from django.urls import path, re_path
from django.conf.urls import url
from . import views

app_name = "foo"
urlpatterns = [
    path('', views.index, name='index'),
    path('hello', views.hello, name='hello'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote')
]
