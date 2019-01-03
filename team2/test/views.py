from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import User

# Create your views here.

class IndexView(generic.ListView):
    model = User
    template_name = 'test/index.html'
    context_object_name = 'user_list'

class DetailView(generic.DetailView):
    model = User
    template_name = 'test/detail.html'