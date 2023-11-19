from django import forms
from projeto.apps.produto.models import Produto


class ProdutoForms(forms.ModelForm):
    class Meta:
        model = Produto
        exclude = ['data_criacao', 'data_modificacao']
        labels = {
            'produto': 'Produto',
            'planta': 'Planta',
            'empilhamento': 'Empilhamento',
            'empilhamento_tipo': 'Tipo de empilhamento',
            'familia': 'Familia',
            'status': 'Status'
        }