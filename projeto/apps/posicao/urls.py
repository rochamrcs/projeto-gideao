from django.urls import path
from projeto.apps.posicao.views import posicao


urlpatterns = [
    path('', posicao, name='posicoes'),
]