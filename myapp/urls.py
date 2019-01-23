from django.urls import path, include
from .views import polls

polls_urls = [
    # ex: /polls/
    path('', polls.index, name="index"),
    # ex: /polls/5/
    path('<int:question_id>/', polls.detail, name="detail"),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', polls.results, name="results"),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', polls.vote, name="vote"),
]

urlpatterns = [
    path('polls/', include((polls_urls, 'polls'), namespace="polls"))
]
