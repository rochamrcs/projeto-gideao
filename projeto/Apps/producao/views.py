from django.views.generic import TemplateView, CreateView, UpdateView, DetailView
from .models import Producao
from .forms import ProducaoForm
from django.urls import reverse_lazy


class ProducaoView(TemplateView):
    template_name = './producao/producao.html'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["producao_lista"] = Producao.objects.all()
        return contexto


class CreateProducao(CreateView):
    template_name = './producao/nova_producao.html'
    form_class = ProducaoForm
    success_url = reverse_lazy('producao')


class DetailProducao(DetailView):
    template_name = './producao/detalhe_producao.html'
    model = Producao

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["producao_lista"] = Producao.objects.all()
        return contexto
