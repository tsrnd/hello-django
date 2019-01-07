from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    text = """Nothing here!"""
    return HttpResponse(text)