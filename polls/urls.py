from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('add/', views.QuestionView.as_view(), name='add'),
    path('<int:pk>/edit/', views.UpdateQuestion.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteQuestion.as_view(), name='delete'),
    path('questions/', views.question_list),
    path('questions/<int:pk>/', views.question_detail),
]
