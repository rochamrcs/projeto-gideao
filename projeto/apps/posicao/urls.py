from django.urls import path
from projeto.apps.posicao.views import posicao, nova_posicao, buscar_posicoes


urlpatterns = [
    path('', posicao, name='posicoes'),
    path('<int:page>', posicao, name='posicao_pagina'),
    path('nova_posicao', nova_posicao, name='nova_posicao'),
    path('buscar_posicoes/', buscar_posicoes, name='buscar_posicoes'),
]