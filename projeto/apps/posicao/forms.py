from django import forms
from projeto.apps.posicao.models import Posicao


class PosicaoForms(forms.ModelForm):

    class Meta:
        model = Posicao
        exclude = ['data_criacao', 'data_modificacao']
        labels = {
            'posicao': 'Posição',
            'planta': 'Planta',
            'capacidade': 'Capacidade',
            'armazenado': 'Armazenado',
            'ocupacao': 'Ocupação',
            'disponibilidade': 'Disponibilidade',
            'status': 'Status'
        }
        widgets = {
            'posicao': forms.TextInput(attrs={'class':'form-control mb-2'}),
            'planta': forms.Select(attrs={'class':'form-select form-select-sm mb-2'}),
            'capacidade': forms.NumberInput(attrs={'class':'form-control mb-2'}),
            'armazenado': forms.NumberInput(attrs={'class':'form-control mb-2'}),
            'ocupacao': forms.NumberInput(attrs={'class':'form-control mb-2'}),
            'disponibilidade': forms.NumberInput(attrs={'class':'form-control mb-2'})
        }