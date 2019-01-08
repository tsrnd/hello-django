from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from .models import Question
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.utils import timezone


def vote(request, question_id):
    # return HttpResponse("You are vote on question %s" % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't section a choice",
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id, )))


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """ Return the last five published question """
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'


class QuestionView(generic.CreateView):
    model = Question
    fields = ['question_text', 'pub_date']
    template_name = 'polls/add.html'


class UpdateQuestion(generic.UpdateView):
    model = Question
    fields = ['question_text']
    template_name = 'polls/edit.html'


class DeleteQuestion(generic.DeleteView):
    model = Question
    success_url = reverse_lazy('polls:index')
