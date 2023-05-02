from django.shortcuts import render
from .models import Posicao

def estoque(request):
    template_name = './estoque/estoque.html'
    objetos = Posicao.objects.all()
    contexto = {'objetos_lista': objetos}
    return render(request, template_name, contexto)