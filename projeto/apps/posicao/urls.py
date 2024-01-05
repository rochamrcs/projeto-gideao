from django.urls import path
from projeto.apps.posicao.views import posicao, nova_posicao, buscar_posicoes, detalhe_posicao, editar_posicao

urlpatterns = [
    path('', posicao, name='posicoes'),
    path('<int:page>', posicao, name='posicao_pagina'),
    path('nova_posicao', nova_posicao, name='nova_posicao'),
    path('buscar_posicoes/', buscar_posicoes, name='buscar_posicoes'),
    path('<int:pk>/', detalhe_posicao, name='detalhe_posicao'),
    path('editar/<int:posicao_id>', editar_posicao, name='editar_posicao')
]