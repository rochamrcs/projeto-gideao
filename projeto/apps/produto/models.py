from django.db import models
from projeto.constants.constants import FAMILIA, PLANTA, EMPILHAMENTO, EMPILHAMENTO_TIPO, STATUS

class Produto(models.Model):


    produto = models.CharField(max_length=20, unique=True)
    planta = models.CharField(max_length=3, choices=PLANTA)
    empilhamento = models.BooleanField(choices=EMPILHAMENTO)
    empilhamento_tipo = models.CharField(max_length=3, choices=EMPILHAMENTO_TIPO)
    familia = models.CharField(max_length=3, choices=FAMILIA)
    status = models.BooleanField(max_length=3, choices=STATUS)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.produto