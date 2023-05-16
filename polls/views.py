from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice


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
    return HttpResponse("resultados: " + str(question_id))


def vote(request, question_id):
    return HttpResponse("votacion: " + str(question_id))