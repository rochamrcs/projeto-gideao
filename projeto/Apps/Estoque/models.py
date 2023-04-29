from django.db import models


class Posicao(models.Model):
    posicao = models.CharField(max_length=30, default="")
    capacidade = models.IntegerField()

    def __str__(self):
        return self.posicao
