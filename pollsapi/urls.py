from django.urls import path
from .views import polls_list, polls_detail
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote

urlpatterns = [
    # path("", polls_list, name="polls_list"),
    # path("<int:poll_id>/", polls_detail, name="polls_detail")
    path("", PollList.as_view(), name="polls_list"),
    path("<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path(
        "<int:pk>/choices/<int:choice_pk>/vote/",
        CreateVote.as_view(),
        name="create_vote"),
]
