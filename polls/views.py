from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from .models import Question
from django.http import HttpResponse


# Create your views here.
def detail(request, question_id):
    return HttpResponse("You 're looking at question %s" % question_id)


def results(request, question_id):
    response = "You are looking at the result question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You are vote on question %s" % question_id)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
