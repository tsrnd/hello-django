from django.conf.urls import url
from django.core.cache import cache
from . import views
from api.category.handler import Handler
from api.category.usecase import Usecase
from api.category.repository import Repository

cate_view = Handler.as_view(view_factory=Usecase(
    repository=Repository(cache)))
urlpatterns = [
    url(r'^$', cate_view),
]
