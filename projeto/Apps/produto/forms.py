from django import forms
from.models import Produto

class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ['produto', 'planta', 'tipo']


class AtualizarProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ['status']