from django.db import models

PLANTA = [
    ('', 'Selecione'),
    ('PE', 'PE9'),
    ('PP', 'PP5'),
]

TIPO = [
    ('', 'Selecione'),
    ('IN', 'INSUMO'),
    ('PA', 'PRODUTO ACABADO')
]

class Produto(models.Model):
    produto = models.CharField(max_length=30, default="", unique=True, error_messages={
        'unique': 'Essa já foi cadastrado.'
    })
    planta = models.CharField(max_length=2, choices=PLANTA, default="Selecione")
    tipo = models.CharField(max_length=2, choices=TIPO, default="Selecione")
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.criado_em.strftime('%d/%m/%Y %H:%M:%S')
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Protudos'
        db_table = 'produtos'

