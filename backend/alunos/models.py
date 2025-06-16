from django.db import models
from django.contrib.auth.models import User

class Aluno(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'alunos'

    def __str__(self):
        return str(self.id)
