import json

from django.views import View
from django.http import HttpResponse

from api.category.usecase import Usecase
from api.category.repository import Repository


class Handler(View):
    view_factory = Usecase(repository=None)

    def get(self, request, *args, **kwargs):
        cates = self.view_factory.get_all_category()
        return HttpResponse(json.dumps(cates), status=200, content_type='application/json')
