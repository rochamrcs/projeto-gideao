from django.urls import path
from projeto.apps.produto.views import produto

urlpatterns = [
    path('', produto, name='produto'),
]