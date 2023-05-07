from django.urls import path
from projeto.Apps.Estoque import views

urlpatterns = [
    path('', views.EstoqueView.as_view(), name='estoque'),
    path('nova_posicao/', views.CriarPosicao.as_view(), name='nova_posicao'),
    path('detail/<str:pk>/', views.DetailPosicao.as_view(), name='detalhe')
]