from django.urls import path
from projeto.apps.produto.views import produto, novo_produto, buscar_produto, detalhe_produto, editar_produto


urlpatterns = [
    path('', produto, name='produtos'),
    path('<int:page>', produto, name='produtos_pagina'),
    path('novo_produto', novo_produto, name='novo_produto'),
    path('buscar_produto/', buscar_produto, name='buscar_produto'),
    path('<int:pk>/', detalhe_produto, name='detalhe_produto'),
    path('editar/<int:produto_id>', editar_produto, name='editar_produto')
]