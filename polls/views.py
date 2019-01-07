from django.shortcuts import render, get_object_or_404
from .models import Question
from django.db.models import F
from django.http import Http404,  HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(
                    pub_date__lte=timezone.now()
                ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    

def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selectedChoice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, question.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selectedChoice.votes = F('votes') + 1
        selectedChoice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))

def basehome(request):
    template = 'base.html'
    context = locals()
    return render(request, template, context)