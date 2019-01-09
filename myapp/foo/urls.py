from django.urls import path, re_path
from django.conf.urls import url
from . import views

app_name = "foo"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('hello', views.hello, name='hello'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote')
]
