from django.shortcuts import render

# Create your views here.
from .models import Topic
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TopicSerializer


class TopicList(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TopicSerializer

    def get_queryset(self):
        return Topic.objects.all().filter(id=self.request.id)


@api_view(['GET', 'PUT', 'DELETE'])
def topic_detail(request, pk):
    """
    Retrieve, update or delete a topic instance.
    """
    try:
        topic = Topic.objects.get(id=pk)
    except Topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TopicSerializer(topic)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TopicSerializer(topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)