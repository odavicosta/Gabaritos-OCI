from django.urls import path
from . import views

urlpatterns = [
    path('<int:aluno_id>/', views.detalhe_aluno, name='detalhe_aluno'),
]
