from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from . leitor_interface import ler_prova_por_dados
from django.http import JsonResponse
import os




@login_required
def index(request):
    if request.method == 'POST' and 'imagem' in request.FILES:
        imagem = request.FILES['imagem']
        dados_bytes = imagem.read()
        extensao = os.path.splitext(imagem.name)[1]
        resultado = ler_prova_por_dados(extensao, dados_bytes)
        return JsonResponse(resultado)  

    return render(request, 'home/home.html')


