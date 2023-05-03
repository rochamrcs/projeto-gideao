from django import forms
from.models import Posicao

class PosicaoForm(forms.ModelForm):

    class Meta:
        model = Posicao
        fields = ['posicao', 'capacidade']
