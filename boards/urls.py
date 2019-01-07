from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('boards/<int:id_board>', views.board_topics, name='board_topics'),
    path('boards/<int:id_board>/add', views.add_topic, name='add_topic'),
]
