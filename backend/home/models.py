from django.db import models
from alunos.models import Aluno

class Prova(models.Model):
    modalidade = models.CharField(max_length=30, default='nenhuma')
    fase = models.IntegerField(default=1)

    class Meta:
        db_table = 'provas'

    def __str__(self):
        return str(self.id)

    
class Gabarito(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, db_column='id_alunos')
    prova = models.ForeignKey(Prova, on_delete=models.CASCADE, db_column ='id_prova')
    leitura = models.CharField(max_length=255)
    erro = models.IntegerField()

    class Meta:
        db_table = 'gabaritos'
    
    def __str__(self):
        return f'Aluno {self.aluno.id} - Prova {self.prova.id}'
