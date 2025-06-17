from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User

class MeuFormularioDeCadastro(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

def cadastro(request):
    #verifica se o usuário enviou alguma informação
    if request.method == "POST":
        #preenche formulário de cadastro
        form = MeuFormularioDeCadastro(request.POST)
        #verifica se o formulário é válido
        if form.is_valid():
            user = form.save()
            # loga o usuário automaticamente após o cadastro
            login(request, user)  
            # redireciona para a página inicial
            return redirect('home')
    else:
        #devolve o formulário vazio
        form = MeuFormularioDeCadastro()

    return render(request, 'cadastro/cadastro.html', {'form': form})
