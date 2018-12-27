from django.shortcuts import render

# Create your views here.
from .models import Topic
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
 
from .serializers import TopicSerializer
 
 
class TopicList(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
 
 
class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TopicSerializer
 
    def get_queryset(self):
        return Topic.objects.all().filter(text=self.request.text)