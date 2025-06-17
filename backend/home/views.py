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
            


           
            gabarito = Gabarito(
                            aluno=aluno,
                            prova=prova,
                            leitura=resultado['leitura'],
                            erro=resultado['erro'],
                        )
            form = GabaritoForm(instance=gabarito)


            return render(request, 'home/confirmar_dados.html', {'form': form})

        # Caso 2: Confirmação e envio do formulário
        else:
            form = GabaritoForm(request.POST)
            if form.is_valid():
                gabarito = form.save(commit=False)
                gabarito.usuario = request.user
                gabarito.save()
                
                return redirect('home')  # Ou uma página de sucesso
            else:
                erro = int(request.POST.get("erro", -1))  # ou outro valor padrão

                mensagem_erro = {
                0: "✓ Leitura bem-sucedida.",
                1: "⚠ Erro de leitura do código Aztec.",
                2: "⚠ Erro na identificação da área de leitura.",
                3: "✖ Erro fatal durante a leitura."
                }.get(erro, "Erro desconhecido.")

               

                return render(request, 'home/confirmar_dados.html', {
                    'form': form,
                    'mensagem_erro': mensagem_erro

                })

   
    # GET: mostra só os alunos do usuário logado
    gabaritos = Gabarito.objects.filter(usuario=request.user)

    return render(request, 'home/home.html', {'gabaritos': gabaritos})
    
