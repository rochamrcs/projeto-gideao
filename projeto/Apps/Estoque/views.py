from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView, DetailView
from .models import Posicao, Armazenamento
from .forms import PosicaoForm
from django.urls import reverse_lazy

def estoque(request):
    template_name = './estoque/estoque.html'
    objetos= Posicao.objects.all()
    contexto = {'objetos_lista': objetos}
    return render(request, template_name, contexto)


def nova_posicao(request):
    template_name = './estoque/nova_posicao_form.html'
    return render(request, template_name)

class CriarPosicao(CreateView):
    template_name = './estoque/nova_posicao_form.html'
    form_class = PosicaoForm
    success_url = reverse_lazy('estoque')

#class DetalhePosicao(DetailView):
#    template_name = './estoque/detail_posicao.html'
#    model = Posicao
#    queryset = Posicao.objects.all()

def detail_estoque(request, pk):
    template_name = './estoque/detail_posicao.html'
    objetos_posicao = Posicao.objects.get(id=pk)
    objetos_armazem = Armazenamento.objects.all()
    contexto = {'objetos_pos': objetos_posicao, 'objetos_arm':  objetos_armazem}
    return render(request, template_name, contexto)
