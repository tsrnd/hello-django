from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from .models import Question
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from polls.models import Question
from polls.serializers import QuestionSerializer


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


@csrf_exempt
def question_list(request):
    if request.method == 'GET':
        question = Question.objects.all()
        serializer = QuestionSerializer(question, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def question_detail(request, pk):
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serialiser = QuestionSerializer(question)
        return JsonResponse(serialiser.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serialiser = QuestionSerializer(question, data=data)
        if serialiser.is_valid():
            serialiser.save()
            return JsonResponse(serialiser.data)
        return JsonResponse(serialiser.errors, status=400)
    elif request.method == 'DELETE':
        question.delete()
        return HttpResponse(status=204)
