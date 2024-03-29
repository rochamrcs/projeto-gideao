from django.db import models
from projeto.constants.constants import FAMILIA, PLANTA, EMPILHAMENTO, EMPILHAMENTO_TIPO, STATUS

class Produto(models.Model):


    produto = models.CharField(max_length=20, unique=True)
    planta = models.CharField(max_length=5, choices=PLANTA)
    empilhamento = models.CharField(choices=EMPILHAMENTO)
    empilhamento_tipo = models.CharField(max_length=9, choices=EMPILHAMENTO_TIPO, default='NA')
    familia = models.CharField(max_length=5, choices=FAMILIA)
    status = models.CharField(max_length=7, choices=STATUS, default='Ativo')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.produto