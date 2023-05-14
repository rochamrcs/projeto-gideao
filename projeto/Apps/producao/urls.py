from django.urls import path
from projeto.Apps.producao import views

urlpatterns = [
    path('', views.ProducaoView.as_view(), name='producao'),
    path('novo_producao/', views.CreateProducao.as_view(), name='nova_producao')
]