from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from projeto.apps.posicao.forms import PosicaoForms
from .models import Posicao

def posicao(request):

    posicao_list = Posicao.objects.all().order_by('posicao')
    paginator = Paginator(posicao_list, 6)

    page = request.GET.get('page')
    posicoes = paginator.get_page(page)
    
    return render(request, 'posicoes/posicoes.html', {'posicoes': posicoes})

def nova_posicao(request):

    form = PosicaoForms()

    if request.method == 'POST':
        form = PosicaoForms(request.POST)
        if form.is_valid():
            form.save()

            return redirect('posicoes')

    return render(request, 'posicoes/posicoes_cad.html', {'form':form})

def buscar_posicoes(request):
    query = request.GET.get('buscar_posicoes')

    if not query:
        posicoes = Posicao.objects.all().order_by('posicao')
        paginator = Paginator(posicoes, 6)

        page = request.GET.get('page')
        posicoes = paginator.get_page(page)
        return render(request, 'posicoes/posicoes.html', {'posicoes': posicoes})
    
    resultados = Posicao.objects.filter(
        Q(posicao__icontains=query) |
        Q(planta__icontains=query)
    ).distinct().order_by('posicao')

    paginator = Paginator(resultados, 6)

    page = request.GET.get('page')
    resultados = paginator.get_page(page)
    return render(request, 'posicoes/posicoes.html', {'posicoes': resultados})