from django.db import models

class Aluno(models.Model):
    class Meta:
        db_table = 'alunos'

    def __str__(self):
        return str(self.id)
