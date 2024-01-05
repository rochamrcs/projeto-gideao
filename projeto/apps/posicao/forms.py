from django import forms
from projeto.apps.posicao.models import Posicao


class PosicaoForms(forms.ModelForm):

    class Meta:
        model = Posicao
        exclude = ['data_criacao', 'data_modificacao']
        labels = {
            'posicao': 'Posição',
            'planta': 'Planta',
            'area': 'Área de armazenamento',
            'capacidade': 'Capacidade',
            'armazenado': 'Armazenado',
            'ocupacao': 'Ocupação',
            'disponibilidade': 'Disponibilidade',
            'status': 'Status'
        }

        widgets = {
            'posicao': forms.TextInput(attrs={'class':'form-control mb-2'}),
            'planta': forms.Select(attrs={'class':'form-select form-select-sm mb-2'}),
            'area': forms.Select(attrs={'class':'form-select form-select-sm mb-2'}),
            'capacidade': forms.NumberInput(attrs={'class':'form-control mb-2'}),
            'armazenado': forms.NumberInput(attrs={'class':'form-control mb-2'}),
            'ocupacao': forms.NumberInput(attrs={'class':'form-control mb-2'}),
            'disponibilidade': forms.NumberInput(attrs={'class':'form-control mb-2'}),
            'status': forms.Select(attrs={'class':'form-select form-select-sm mb-2'})
        }

    def clean_capacidade(self):
        capacidade = self.cleaned_data.get('capacidade')
        if capacidade <= 0:
            raise forms.ValidationError("A capacidade deve ser maior que zero.")
        return capacidade
    
    def clean_posicao(self):
        posicao = self.cleaned_data.get('posicao')
        existe_posicao = Posicao.objects.exclude(id=self.instance.id).filter(posicao=posicao).exists()
        
        if existe_posicao:
            raise forms.ValidationError("Essa posição já existe com essa identificação.")
        return posicao
