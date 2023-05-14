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

STATUS = [
    ('A', 'Ativo'),
    ('I', 'Inativo')
]


class Produto(models.Model):
    produto = models.CharField(max_length=30, default="", unique=True, error_messages={
        'unique': 'Essa já foi cadastrado.'
    })
    planta = models.CharField(max_length=2, choices=PLANTA, default="Selecione")
    tipo = models.CharField(max_length=2, choices=TIPO, default="Selecione")
    status = models.CharField(max_length=2, choices=STATUS, default="Ativo")
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.produto
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Protudos'
        db_table = 'produtos'

