from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse


# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    context = {'q': q}
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    context = {'q': q}
    return render(request, 'polls/results.html', context)


def vote(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    try:
        opcion = q.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {'q': q}
        return render(request, 'polls/detail.html', context)
    else:
        opcion.votes += 1
        opcion.save()
    return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))
