from django.shortcuts import render
from .models import Job
# Create your views here.
def index(request):
    jobs = Job.objects
    return render(request, 'blog/index.html', {'jobs': jobs})
