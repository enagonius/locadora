from django.contrib import admin
from core.models import (
    Diretor,
    Roteirista,
    Filme,
    Genero,
    Direcao,
    Roteiro,
    Classificacao,
    Cliente,
    TelefoneCliente,
    Aluguel
)

model_list = (
    Diretor,
    Roteirista,
    Filme,
    Genero,
    Direcao,
    Roteiro,
    Classificacao,
    Cliente,
    TelefoneCliente,
    Aluguel
)


for model in model_list:
    admin.site.register(model, admin.ModelAdmin)
