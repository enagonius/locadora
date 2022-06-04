from django.db import models


class Diretor(models.Model):
    nome = models.CharField(max_length=255, db_index=True)

    class Meta:
        verbose_name_plural = "Diretores"


class Roteirista(models.Model):
    nome = models.CharField(max_length=255, db_index=True)


class Filme(models.Model):
    titulo = models.CharField(max_length=255, db_index=True)
    data_de_lancamento = models.DateField()
    sinopse = models.TextField()
    qtd_copias = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.titulo


class Genero(models.Model):
    estilo = models.CharField(max_length=255, primary_key=True, db_index=True)

    class Meta:
        verbose_name = "Gênero"


class Direcao(models.Model):
    diretor = models.ForeignKey('core.Diretor', on_delete=models.CASCADE)
    filme = models.ForeignKey('core.Filme', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('diretor', 'filme')
        verbose_name = 'Direção'
        verbose_name_plural = 'Direções'


class Roteiro(models.Model):
    roteirista = models.ForeignKey('core.Roteirista', on_delete=models.CASCADE)
    filme = models.ForeignKey('core.Filme', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('roteirista', 'filme')


class Classificacao(models.Model):
    genero = models.ForeignKey('core.Genero', on_delete=models.CASCADE)
    filme = models.ForeignKey('core.Filme', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('genero', 'filme')
        verbose_name = 'Classificação'
        verbose_name_plural = 'Classificações'


class Cliente(models.Model):
    nome = models.CharField(max_length=255, db_index=True)
    endereco = models.CharField(max_length=255)


class TelefoneCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=16)


class Aluguel(models.Model):
    datetime_aluguel = models.DateTimeField(auto_now_add=True)
    prazo_devolucao = models.DateTimeField()
    datetime_devolucao = models.DateTimeField()
    funcionario = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    cliente = models.ForeignKey('core.Cliente', on_delete=models.DO_NOTHING)
    filme = models.ForeignKey('core.Filme', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = 'Aluguéis'
