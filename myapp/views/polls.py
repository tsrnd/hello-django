from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from myapp.models.polls import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', {
        'latest_question_list': latest_question_list,
    })


def detail(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {question: question})


def results(request, question_id):
    content = "You're looking at the results of question %s."
    return HttpResponse(content % question_id)


def vote(request, question_id):
    content = "You're voting on question %s."
    return HttpResponse(content % question_id)
