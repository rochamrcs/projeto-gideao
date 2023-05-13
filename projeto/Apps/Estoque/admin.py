from django.contrib import admin

from projeto.Apps.Estoque.models import Armazenamento, Posicao

class PosicaoAdmin(admin.ModelAdmin):
    list_display = ('posicao','area', 'capacidade','armazenado', 'ocupacao') #Personaliza a exibição de colunas no painel admin
    ordering = ['posicao'] #Ordena por posição no painel admin


admin.site.register(Posicao, PosicaoAdmin)
admin.site.register(Armazenamento)
