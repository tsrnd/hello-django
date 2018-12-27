from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    response = HttpResponse()
    response.write("<center><h1>Welcome to Other</h1></center>")
    return response
