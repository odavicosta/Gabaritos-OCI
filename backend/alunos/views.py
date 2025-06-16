from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Aluno
from home.models import Gabarito

def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/lista_alunos.html', {'alunos': alunos})

def detalhe_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, pk=aluno_id)
    gabaritos = Gabarito.objects.filter(aluno=aluno)
    return render(request, 'alunos/detalhe_aluno.html', {'aluno': aluno, 'gabaritos': gabaritos})

