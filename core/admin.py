from django.contrib import admin
from core.models import (
    Diretor,
    Roteirista,
    Filme,
    Genero,
    Cliente,
    TelefoneCliente,
    Aluguel
)

model_list = (
    Diretor,
    Roteirista,
    Filme,
    Genero,
    Cliente,
    TelefoneCliente,
    Aluguel
)


for model in model_list:
    admin.site.register(model, admin.ModelAdmin)
