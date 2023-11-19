from django.shortcuts import render, redirect
from projeto.apps.produto.forms import ProdutoForms


def produto(request):
    form = ProdutoForms()

    if request.method == 'POST':
        form = ProdutoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'produto/produto_cad.html', {'form':form})