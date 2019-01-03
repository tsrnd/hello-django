from django.conf.urls import url
from django.core.cache import cache
from myapp.category.handler import Handler
from myapp.category.usecase import Usecase
from myapp.category.repository import Repository

cate_view = Handler.as_view(view_factory=Usecase(
    repository=Repository(cache)))
urlpatterns = [
    url(r'^$', cate_view),
]