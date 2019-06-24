from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from .models import boards,topic,posts
from django.contrib.auth.models import User
from .forms import NewTopicForm,PostForm
from django.contrib.auth.decorators import login_required

# Create your views here

def index (request):

    boardss = boards.objects.all()
    return render(request, 'home.html', {'boards':boardss})    

def boards_topic(request, id):
    
    board = get_object_or_404(boards,pk=id)
    return render(request, 'topics.html', {'boards':board})

@login_required

def new_topic(request , id ):

    board = get_object_or_404(boards,pk=id)
    user = request.user
    if request.method == "POST":
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topics = form.save(commit=False)
            topics.board = board
            topics.created_by = user
            topics.save()
        # subject = request.POST['subject']
        # message = request.POST['message']
        
        # topics = topic.objects.create(subject=subject, created_by=user, board=board)
            post = posts.objects.create(message=form.cleaned_data.get('message'), topic=topics, created_by=user)

        return redirect('boards_topic', id=board.pk)
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'boards':board, 'form':form})

def topic_posts(request ,id, topic_id):
    topics =get_object_or_404(topic, board__pk=id, pk=topic_id)
    return render(request, 'topic_posts.html', {'topic':topics})

@login_required
def reply_topic(request, id , topic_id):
    topics =get_object_or_404(topic, board__pk=id, pk=topic_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topics
            post.created_by = request.user
            post.save()
            return redirect('topic_posts', id=id, topic_id=topics.pk)
    else:
        form = PostForm()
    return render(request, 'reply_topic.html',{'topic':topics, 'form':form})