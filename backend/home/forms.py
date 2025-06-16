from django import forms
from .models import Gabarito

class GabaritoForm(forms.ModelForm):
    class Meta:
        model = Gabarito
        fields = ['aluno', 'prova', 'leitura']