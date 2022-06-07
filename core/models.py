from django.db import models
from django.contrib.auth.models import User


class Diretor(models.Model):
    nome = models.CharField(max_length=255, db_index=True)

    class Meta:
        verbose_name_plural = "Diretores"

    def __str__(self):
        return self.nome

    def get_filme_instances(self):
        return [a for a in self.filme_set.all()]


class Roteirista(models.Model):
    nome = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.nome

    def get_filme_instances(self):
        return [a for a in self.filme_set.all()]

class Genero(models.Model):
    estilo = models.CharField(max_length=255, primary_key=True, db_index=True)

    class Meta:
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"

    def __str__(self):
        return self.estilo


class Filme(models.Model):
    titulo = models.CharField(max_length=255, db_index=True)
    data_de_lancamento = models.DateField()
    sinopse = models.TextField()
    qtd_copias = models.PositiveIntegerField(default=1)
    roteiristas = models.ManyToManyField(Roteirista)
    diretores = models.ManyToManyField(Diretor)
    generos = models.ManyToManyField(Genero)

    class Meta:
        ordering = ('titulo',)

    def __str__(self):
        return self.titulo

    def get_diretores(self):
        return ', '.join([a.nome for a in self.diretores.all()])

    def get_diretores_instances(self):
        return [a for a in self.diretores.all()]

    def get_roteiristas(self):
        return ', '.join([a.nome for a in self.roteiristas.all()])
    
    def get_roteiristas_instances(self):
        return [a for a in self.roteiristas.all()]

    def get_generos(self):
        return ', '.join([a.estilo for a in self.generos.all()])

class Cliente(models.Model):
    nome = models.CharField(max_length=255, db_index=True)
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class TelefoneCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=16)


class Aluguel(models.Model):
    filme = models.ForeignKey('core.Filme', on_delete=models.DO_NOTHING)
    cliente = models.ForeignKey('core.Cliente', on_delete=models.DO_NOTHING)
    funcionario = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    datetime_aluguel = models.DateTimeField(auto_now_add=True)
    prazo_devolucao = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Aluguéis'


class Funcionario(User):
    class Meta:
        proxy = True
