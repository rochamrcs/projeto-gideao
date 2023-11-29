from django.urls import path
from projeto.apps.posicoes.views import posicao


urlpatterns = [
    path('', posicao, name='posicao'),
]