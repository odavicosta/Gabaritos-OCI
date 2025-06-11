from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login



def cadastro(request):
    #verifica se o usuário enviou alguma informação
    if request.method == "POST":
        #preenche formulário de cadastro
        form = UserCreationForm(request.POST)
        #verifica se o formulário é válido
        if form.is_valid():
            user = form.save()
            # loga o usuário automaticamente após o cadastro
            login(request, user)  
            # redireciona para a página inicial
            return redirect('home')
    else:
        #devolve o formulário vazio
        form = UserCreationForm()

    return render(request, 'home/home.html', {'form': form})
