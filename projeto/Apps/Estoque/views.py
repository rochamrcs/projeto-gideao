from typing import Any, Dict
from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, DetailView, CreateView
from .models import Posicao, Armazenamento
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


def detail_estoque(request, pk):
    template_name = './estoque/detail_posicao.html'
    objetos_posicao = Posicao.objects.get(id=pk)
    objetos_armazem = Armazenamento.objects.filter(posicao=objetos_posicao)
    contexto = {'objetos_pos': objetos_posicao, 'objetos_arm':  objetos_armazem}
    return render(request, template_name, contexto)
