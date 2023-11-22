from django.urls import path
from projeto.apps.produto.views import produto, novo_produto, buscar_produto


urlpatterns = [
    path('', produto, name='produtos'),
    path('<int:page>', produto, name='produtos_pagina'),
    path('novo_produto', novo_produto, name='novo_produto'),
    path('buscar_produto/', buscar_produto, name='buscar_produto'), 
]