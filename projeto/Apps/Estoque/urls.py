from django.urls import path
from projeto.Apps.Estoque import views

urlpatterns = [
    path('', views.estoque, name='estoque'),
]