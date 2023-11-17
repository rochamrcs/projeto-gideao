from django.urls import path
from projeto.apps.core.views import home

urlpatterns = [
    path('', home),

]