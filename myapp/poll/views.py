from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    text = """<h1>Nothing here!</h1>"""
    return HttpResponse(text)

def detail(request, question_id):
    content = "You're looking at question %s."
    return HttpResponse(content % question_id)

def results(request, question_id):
    content = "You're looking at the results of question %s."
    return HttpResponse(content % question_id)

def vote(request, question_id):
    content = "You're voting on question %s."
    return HttpResponse(content % question_id)
