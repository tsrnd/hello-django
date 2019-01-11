from django.urls import path
# from .views import polls_list, polls_detail
from .apiviews import PollList, PollDetail, CreateVote, ChoiceList, UserCreate
from .apiviews import PollViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('polls2', PollViewSet, base_name='polls2')

urlpatterns = [
    path('', PollList.as_view(), name="polls_list"),
    path('<int:pk>/', PollDetail.as_view(), name="polls_detail"),
    path('<int:pk>/choices/', ChoiceList.as_view(), name="choice_list"),
    path('<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name="create_vote"),
    path('users/', UserCreate.as_view(), name="user_create"),
]

urlpatterns += router.urls