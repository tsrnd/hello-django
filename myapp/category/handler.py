import json

from django.views import View
from django.http import HttpResponse

from myapp.category.usecase import Usecase
from myapp.category.repository import Repository
import logging

logger = logging.getLogger(__name__)


class Handler(View):
    view_factory = Usecase(repository=None)

    def get(self, request, *args, **kwargs):
        cates, err = self.view_factory.get_all_category()
        if err is not None:
            logger.error(err, "get all category error.")
            return HttpResponse(json.dumps({"message": "Get categories error.", "error": err}), status=500, content_type='application/json')
        return HttpResponse(json.dumps(cates), status=200, content_type='application/json')
