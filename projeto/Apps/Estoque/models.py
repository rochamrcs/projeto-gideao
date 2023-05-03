from django.db import models


class Posicao(models.Model):
    posicao = models.CharField(max_length=30, default="", unique=True, error_messages={
        'unique': 'Essa posição já possui cadastro'
    })
    capacidade = models.IntegerField()
    ocupacao = models.IntegerField(default=0)

    def __str__(self):
        return self.posicao
    
    class Meta:
        verbose_name = 'Posição'
        verbose_name_plural = 'Posições'
        db_table = 'posicoes'

class Armazenamento(models.Model):
    PID = models.CharField(max_length=100, unique=True)
    posicao = models.ForeignKey(Posicao, on_delete=models.PROTECT)
    produto = models.CharField(max_length=25)
    modal = models.CharField(max_length=5)
    criado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.PID
    
    class Meta:
        verbose_name = 'Armazenamento'
        verbose_name_plural = 'Armazenamentos'
        db_table = 'armazenamentos'