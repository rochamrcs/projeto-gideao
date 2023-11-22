from django import forms
from projeto.apps.produto.models import Produto


class ProdutoForms(forms.ModelForm):
    class Meta:
        model = Produto
        exclude = ['data_criacao', 'data_modificacao', 'status']
        labels = {
            'produto': 'Produto',
            'planta': 'Planta',
            'empilhamento': 'Empilhamento',
            'empilhamento_tipo': 'Tipo de empilhamento',
            'familia': 'Familia',
            'status': 'Status'
        }

        widgets = {
            'produto': forms.TextInput(attrs={'class':'form-control mb-2'}),
            'planta': forms.Select(attrs={'class':'form-select form-select-sm mb-2'}),
            'empilhamento': forms.Select(attrs={'class':'form-select form-select-sm mb-2'}),
            'empilhamento_tipo': forms.Select(attrs={'class':'form-select form-select-sm mb-2'}),
            'familia': forms.Select(attrs={'class':'form-select form-select-sm mb-2'}),
            'status': forms.Select(attrs={'class':'form-select form-select-sm mb-2'})
        }