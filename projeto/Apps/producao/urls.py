from django.urls import path
from projeto.Apps.producao import views

urlpatterns = [
    path('', views.ProducaoView.as_view(), name='producao'),
    path('novo_producao/', views.CreateProducao.as_view(), name='nova_producao'),
    path('detalhe_producao/<str:pk>/', views.DetailProducao.as_view(), name='detalhe_producao'),
    path('apontar_producao/<str:pk>/', views.ApontarProducao.as_view(), name ='apontar_producao')
]