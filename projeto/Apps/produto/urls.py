from django.urls import path
from projeto.Apps.produto import views

urlpatterns = [
    path('', views.ProdutoView.as_view(), name='produto')
]