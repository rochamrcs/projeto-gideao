from django.views.generic import TemplateView, CreateView, UpdateView
from .models import Produto
from .forms import ProdutoForm, AtualizarProdutoForm
from django.urls import reverse_lazy


class ProdutoView(TemplateView):
    template_name = './produto/produtos.html'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["produto_lista"] = Produto.objects.all()
        return contexto


class CreateProduto(CreateView):
    template_name = './produto/novo_produto.html'
    form_class = ProdutoForm
    success_url = reverse_lazy('produto')


class AtualizarProduto(UpdateView):
    template_name = './produto/atualizar_produto.html'
    form_class = AtualizarProdutoForm
    model = Produto
    success_url = reverse_lazy('produto')