from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from projeto.constants.constants import PLANTA, STATUS, ARMAZENAMENTO

class Posicao(models.Model):
    
    posicao = models.CharField(max_length=20, unique=True)
    planta = models.CharField(max_length=5, choices=PLANTA)
    area = models.CharField(max_length=7, choices=ARMAZENAMENTO)
    capacidade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)])
    armazenado = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(50)])
    ocupacao = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    disponibilidade = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    status = models.CharField(max_length=7, choices=STATUS, default='Ativo')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Posição"
        verbose_name_plural = "Posições"
        ordering = ['posicao']

    def __str__(self):
        return self.posicao