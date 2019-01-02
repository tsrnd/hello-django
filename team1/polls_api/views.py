"""module import"""
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .models import Poll


def polls_list(request):
    """list poll"""
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {"results": list(polls.values(
        "question", "created_by__username", "pub_date"))}
    return JsonResponse(data)


def polls_detail(request, poll_id):
    """detail poll"""
    poll = get_object_or_404(Poll, pk=poll_id)
    data = {"results": {
        "question": poll.question,
        "created_by": poll.created_by.username,
        "pub_date": poll.pub_date
    }}
    return JsonResponse(data)
