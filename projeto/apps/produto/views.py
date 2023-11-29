from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from projeto.apps.produto.forms import ProdutoForms
from .models import Produto


def produto(request):
    product_list = Produto.objects.all().order_by('data_criacao')
    paginator = Paginator(product_list, 6)

    page = request.GET.get('page')
    produtos = paginator.get_page(page)
    
    return render(request, 'produto/produtos.html', {'produtos':produtos})

def novo_produto(request):

    form = ProdutoForms()

    if request.method == 'POST':
        form = ProdutoForms(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('produtos')

    return render(request, 'produto/produto_cad.html', {'form':form})

def buscar_produto(request):
    query = request.GET.get('buscar_produtos')

    if not query:
        produtos = Produto.objects.all().order_by('data_criacao')
        paginator = Paginator(produtos, 6)

        page = request.GET.get('page')
        produtos = paginator.get_page(page)
        return render(request, 'produto/produtos.html', {'produtos': produtos})


    resultados = Produto.objects.filter(
        Q(produto__icontains=query) |
        Q(familia__icontains=query) |
        Q(planta__icontains=query)
    ).distinct().order_by('data_criacao')

    paginator = Paginator(resultados, 6)

    page = request.GET.get('page')
    resultados = paginator.get_page(page)
    return render(request, 'produto/produtos.html', {'produtos': resultados})

def detalhe_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)

    return render(request, 'produto/produto_detail.html', {'detalhe_produto': produto})

def editar_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)

    form = ProdutoForms(instance=produto)

    if request.method == 'POST':
        form = ProdutoForms(request.POST, instance=produto)
        if form.is_valid:
            form.save()
            return redirect('produtos')
    
    return render(request, 'produto/produto_edit.html', {'form': form, 'produto_id':produto_id})