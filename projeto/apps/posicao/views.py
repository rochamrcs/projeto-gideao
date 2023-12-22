from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Posicao

def posicao(request):

    posicao_list = Posicao.objects.all()
    paginator = Paginator(posicao_list, 6)

    page = request.GET.get('page')
    posicoes = paginator.get_page(page)
    
    return render(request, 'posicoes/posicoes.html', {'posicoes': posicoes})
