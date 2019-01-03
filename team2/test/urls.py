from django.urls import path

from . import views

app_name = 'test'
urlpatterns = [
    # ex: /test/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /test/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]