from django.contrib import admin
from .models import Escola, Prova, Participante, LeituraGabarito

admin.site.register(Escola)
admin.site.register(Prova)
admin.site.register(Participante)
admin.site.register(LeituraGabarito)