from .models import Snippet
from .serializers import SnippetSerializer, StatSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import mixins
from rest_framework import generics

from django.db import connection

import sys


class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        sys.stdout.write('SnippetList get\n')
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        sys.stdout.write('SnippetList post\n')
        return self.create(request, *args, **kwargs)


class SnippetDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        """ Default statement for get Snippet detail.
        sys.stdout.write('SnippetDetail get\n')
        return self.retrieve(request, *args, **kwargs)
        """
        """ Custom SQL statement. """
        sys.stdout.write('Request :\n' + str(request))
        sys.stdout.write('args :\n' + str(args))
        sys.stdout.write('kwargs :\n' + str(kwargs))
        """with connection.cursor() as cursor:
            cursor.execute("SELECT title, language FROM tbl_snipplet WHERE id = %s", request.GET.get('pk',''))
            row = cursor.fetchone()

        return row"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        sys.stdout.write('SnippetDetail put\n')
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        sys.stdout.write('SnippetDetail delete\n')
        return self.destroy(request, *args, **kwargs)


class SnipListView(ListAPIView):
    queryset = Snippet.objects.raw(
        "SELECT id, title FROM tbl_snipplet GROUP BY id, title order by count(*) desc LIMIT 10"
    )
    serializer_class = StatSerializer

    def list(self, request):
        queryset = self.get_queryset()
        # the serializer didn't take my RawQuerySet, so made it into a list
        serializer = StatSerializer(list(queryset), many=True)
        return Response(serializer.data)

class JoinListView(ListAPIView):
    queryset = Snippet.objects.raw(
        "SELECT id, title FROM tbl_snipplet GROUP BY id, title order by count(*) desc LIMIT 10"
    )
    serializer_class = StatSerializer

    def list(self, request):
        queryset = self.get_queryset()
        # the serializer didn't take my RawQuerySet, so made it into a list
        serializer = StatSerializer(list(queryset), many=True)
        return Response(serializer.data)