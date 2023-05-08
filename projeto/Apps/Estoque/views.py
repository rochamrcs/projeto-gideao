from django.views.generic import TemplateView, DetailView, CreateView
from .models import Posicao
from .forms import PosicaoForm
from django.urls import reverse_lazy


class EstoqueView(TemplateView):
    template_name = './estoque/estoque.html'
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["objetos_lista"] = Posicao.objects.all()
        return contexto


class CriarPosicao(CreateView):
    template_name = './estoque/nova_posicao_form.html'
    form_class = PosicaoForm
    success_url = reverse_lazy('estoque')


class DetailPosicao(DetailView):
    template_name = './estoque/detail_posicao.html'
    model = Posicao

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["objetos_lista"] = Posicao.objects.all()
        return contexto
