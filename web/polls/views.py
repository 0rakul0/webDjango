from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse ("olá")

def detail(request, question_id):
    return HttpResponse('Essta é a pergunta {}'.format(question_id))

def results(request, question_id):
    return HttpResponse ('A resposta correta é: {} '.format(question_id))

def vote(request, question_id):
    return HttpResponse ('Seu voto é para para a pergunta {}'.format(question_id))