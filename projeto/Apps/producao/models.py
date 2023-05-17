from django.db import models
from projeto.Apps.produto.models import Produto, PLANTA
from .validator import validar_ordem, valida_lote, valida_volume

MODAL = [   
    ('','Selecione'),
    ('PL','PL14'),
    ('BR','BR25'),
    ('RR','BRR25')
]

STATUS = [
    ('', 'Selecione'),
    ('P','Pendente'),
    ('E','Em andamento'),
    ('F','Finalizado')
]

class Producao(models.Model):
    ordem = models.CharField(max_length=8, validators=[validar_ordem], unique=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    lote = models.CharField(max_length=10, validators=[valida_lote], unique=True)
    planta = models.CharField(max_length=2, choices=PLANTA)
    modal = models.CharField(max_length=5, choices=MODAL)
    linha = models.CharField(max_length=15)
    volume = models.CharField(max_length=6,validators=[valida_volume])
    status = models.CharField(max_length=12, choices=STATUS, default='P')
    ensacado = models.CharField(max_length=6, default=0)
    

    def __str__(self):
        return str(self.ordem)
    
    class Meta:
        verbose_name = 'Produção'
        verbose_name_plural = 'Produções'

    def save(self, *args,**kwargs):
        self.lote = self.lote.upper()
        super(Producao, self).save(*args, **kwargs)