from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Board, Topic, Post
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, id_board=None):
    try:
        board = Board.objects.get(pk=id_board)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})

def add_topic(request, id_board):
    board = get_object_or_404(Board, pk=id_board)

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first()

        topic = Topic.objects.create(
            subject=subject,
            board=board,
            starter=user
        )

        post = Post.objects.create(
            message=message,
            topic=topic,
            created_by=user
        )

        return redirect('board_topics', id_board=board.pk)

    return render(request, 'add_topic.html', {'board': board})
