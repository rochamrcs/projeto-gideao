from django.contrib import admin
from .models import Posicao

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('posicao', 'planta', 'area', 'capacidade', 'armazenado', 'ocupacao', 'disponibilidade', 'status', 'formatted_data_criacao', 'formatted_data_modificacao')
    list_filter = ('area', 'planta', 'status')

    def formatted_data_criacao(self, obj):
        return obj.data_criacao.strftime("%d/%m/%Y %H:%M") if obj.data_criacao else None

    def formatted_data_modificacao(self, obj):
        return obj.data_modificacao.strftime("%d/%m/%Y %H:%M") if obj.data_modificacao else None

    formatted_data_criacao.short_description = 'Data de Criação'  # Define o nome da coluna no admin
    formatted_data_modificacao.short_description = 'Última Modificação'  # Define o nome da coluna no admin

admin.site.register(Posicao, ProdutoAdmin)