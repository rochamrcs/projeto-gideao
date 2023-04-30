from django.contrib import admin

from projeto.Apps.Estoque.models import Posicao

class PosicaoAdmin(admin.ModelAdmin):
    list_display = ('posicao', 'capacidade') #Personaliza a exibição de colunas no painel admin
    ordering = ['posicao'] #Ordena por posição no painel admin

admin.site.register(Posicao, PosicaoAdmin)
