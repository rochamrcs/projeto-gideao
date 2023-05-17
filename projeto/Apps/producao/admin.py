from django.contrib import admin
from projeto.Apps.producao.models import Producao

class ProducaoAdmin(admin.ModelAdmin):
    list_display = ('ordem', 'produto','modal', 'lote', 'planta', 'linha', 'volume','ensacado','status')
    ordering = ['ordem']

admin.site.register(Producao, ProducaoAdmin)