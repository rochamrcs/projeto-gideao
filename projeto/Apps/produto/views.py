from typing import Any, Dict
from django.views.generic import TemplateView
from .models import Produto


class ProdutoView(TemplateView):
    template_name = './produto/produtos.html'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["produto_lista"] = Produto.objects.all()
        return contexto
