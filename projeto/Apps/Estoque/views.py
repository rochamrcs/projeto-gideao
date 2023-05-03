from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView, DetailView
from .models import Posicao
from .forms import PosicaoForm
from django.urls import reverse_lazy

def estoque(request):
    template_name = './estoque/estoque.html'
    objetos = Posicao.objects.all()
    contexto = {'objetos_lista': objetos}
    return render(request, template_name, contexto)

def nova_posicao(request):
    template_name = './estoque/nova_posicao_form.html'
    return render(request, template_name)

class CriarPosicao(CreateView):
    template_name = './estoque/nova_posicao_form.html'
    form_class = PosicaoForm
    success_url = reverse_lazy('estoque')

class DetalhePosicao(DetailView):
    template_name = './estoque/detail_posicao.html'
    model = Posicao
    queryset = Posicao.objects.all()
