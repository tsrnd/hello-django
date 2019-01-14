from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views import generic
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question, Choice, QuestionSerializer



class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'lastest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('pub_date')[:5]

def hello(request):
    text = """<h1>Hello Django!</h1>"""
    return HttpResponse(text)


class DetailView(generic.DetailView):
    model = Question
    template_name = 'detail.html'


class ResultView(generic.DetailView):
    model = Question
    template_name = 'results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('foo:results', args=(question.id,)))

class QuestionListView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serial = QuestionSerializer(questions, many=True)
        # data = []
        # for question in questions:
        #     data.append({
        #         'question_id': question.id,
        #         'question_text': question.question_text
        #     })
        return Response(serial.data, status=404)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        print(serializer.is_valid(), serializer.errors)
        ques = serializer.save()
        resp = QuestionSerializer(ques)
        return Response(resp.data, status=200)
    
    def put(self, request, pk=None, format=None):
        question = get_object_or_404(Question, pk=pk)
        serializer = QuestionSerializer(question, data=request.data)
        # print(serializer.is_valid(), serializer.errors)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)
