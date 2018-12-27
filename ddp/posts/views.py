from django.views.generic import ListView
from .models import Post
from .serializers import PostSerializer

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(topic=self.request.topic)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all().filter(topic=self.request.topic)
