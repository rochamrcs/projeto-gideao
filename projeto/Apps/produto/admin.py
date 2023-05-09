from django.contrib import admin

from projeto.Apps.produto.models import Produto


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'planta', 'tipo', 'criado_em', 'modificado_em')
    ordering = ['produto']

admin.site.register(Produto, ProdutoAdmin)