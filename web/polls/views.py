from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Question


# Create your views here.

def index(request):
    lista_questoes_criadas = Question.objects.order_by('pub_date')[:5]
    context = {'lista_questoes_criadas': lista_questoes_criadas}
    return render(request, 'polls/index.html', context)

def results(request, question_id):
    question = Question(pk=question_id)
    return render(request, 'polls/results.html', {'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selecionar_mudanca = question.mudanca_set.get(pk=request.POST['mudanca'])
    except KeyError:
        return render(request, 'polls:vote.html',{
            'question':question,
            'erro_message':"não foi possivel achar seu voto.",
        })
    else:
        selecionar_mudanca.voto +=1
        selecionar_mudanca.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))