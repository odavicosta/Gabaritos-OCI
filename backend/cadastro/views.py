from django.shortcuts import render

def index(request):
    return render(request,'cadastro/cadastro.html')

# Create your views here.
