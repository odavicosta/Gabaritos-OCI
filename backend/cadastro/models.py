from django.db import models

class Escola(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    estado = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return self.nome

class Prova(models.Model):
    modalidade = models.CharField(max_length=30) # Ex: "Nível 1"
    fase = models.PositiveIntegerField() # Ex: 1 ou 2
    data_prova = models.DateField(blank=True, null=True)
    gabarito_oficial = models.JSONField(default=dict) 
    # Ex: {"1": "A", "2": "C", "3": "B", ...}

    def __str__(self):
        return f"{self.modalidade} - Fase {self.fase}"

class Participante(models.Model):
    nome = models.CharField(max_length=60)
    cpf = models.CharField(max_length=11, unique=True) # CPF deve ser único
    escola = models.ForeignKey(Escola, on_delete=models.SET_NULL, null=True, blank=True)
    # on_delete=models.SET_NULL: Se uma escola for apagada, o campo 'escola' no participante vira nulo. O participante não é apagado.

    def __str__(self):
        return self.nome

class LeituraGabarito(models.Model):
    # Juntei Gabaritos e Respostas em um só modelo para simplificar.
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    prova = models.ForeignKey(Prova, on_delete=models.CASCADE)
    # on_delete=models.CASCADE: Se o participante ou a prova forem apagados, esta leitura também será.
    respostas_aluno = models.JSONField(default=dict) # Ex: {"1": "A", "2": "D", ...}
    nota = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    acertos = models.IntegerField(null=True, blank=True)
    erros = models.IntegerField(null=True, blank=True)
    
    class Meta:
        # Garante que um aluno não pode ter dois gabaritos para a mesma prova.
        unique_together = ('participante', 'prova')

    def __str__(self):
        return f"Gabarito de {self.participante.nome} para {self.prova}"