from django import forms
from.models import Producao

class ProducaoForm(forms.ModelForm):

    class Meta:
        model = Producao
        fields = ['ordem', 'produto','modal', 'lote', 'planta', 'linha', 'volume','status']