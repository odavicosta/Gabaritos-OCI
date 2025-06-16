from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import GabaritoForm
from .models import Gabarito, Aluno, Prova
from .leitor_interface import ler_prova_por_dados
from django.contrib.auth.models import User
import os

@login_required
def index(request):
    if request.method == 'POST':
        # Caso 1: Upload de imagem
        if 'imagem' in request.FILES:
            imagem = request.FILES['imagem']
            dados_bytes = imagem.read()
            extensao = os.path.splitext(imagem.name)[1]
            resultado = ler_prova_por_dados(extensao, dados_bytes)

            aluno, _ = Aluno.objects.get_or_create(id=resultado["id_participante"])
            prova, _ = Prova.objects.get_or_create(id=resultado["id_prova"])
            
            # Preenche o formulário com os dados lidos
            form = GabaritoForm(initial={
                'aluno': resultado['id_participante'],
                'prova': resultado['id_prova'],
                'leitura': resultado['leitura'],
                'erro': resultado['erro'],
            })

            return render(request, 'home/confirmar_dados.html', {'form': form})

        # Caso 2: Confirmação e envio do formulário
        else:
            form = GabaritoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')  # Ou uma página de sucesso
            else:
                mensagem_erro = {
                0: "✓ Leitura bem-sucedida.",
                1: "⚠ Erro de leitura do código Aztec.",
                2: "⚠ Erro na identificação da área de leitura.",
                3: "✖ Erro fatal durante a leitura."
                }.get(resultado['erro'], "Erro desconhecido.")

                return render(request, 'home/confirmar_dados.html', {
                    'form': form,
                    'mensagem_erro': mensagem_erro

                })

    # GET: exibe lista de alunos na home
    alunos = Aluno.objects.all()
    return render(request, 'home/home.html', {'alunos': alunos})
