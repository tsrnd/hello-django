from django.urls import path
from django.core.cache import cache
from myapp.category.handler import Handler
from myapp.category.usecase import Usecase
from myapp.category.repository import Repository
from django.views.generic.base import TemplateView
cate_view = Handler.as_view(view_factory=Usecase(repository=Repository(cache)))
urlpatterns = [
    path('', cate_view),
    path(
        'create',
        TemplateView.as_view(template_name='category/create.html'),
        name='template'),
]
