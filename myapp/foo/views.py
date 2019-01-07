from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader
from .models import Question


def index(request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    teamplate = loader.get_template("index.html")
    context = {
        'lastest_question_list': lastest_question_list,
    }
    return HttpResponse(teamplate.render(context, request))

def hello(request):
    text = """<h1>Hello Django!</h1>"""
    return HttpResponse(text)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at results of question %s." % question_id
    return HttpResponse(response)


def vote(request, question_id):
    response = "You're voting on question %s." % question_id
    return HttpResponse(response)
