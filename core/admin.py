from django.contrib import admin
from .models import Cliente, NotaFiscal

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display  = ('nome', 'cpf_cnpj', 'email')
    search_fields = ('nome', 'cpf_cnpj')

@admin.register(NotaFiscal)
class NotaFiscalAdmin(admin.ModelAdmin):
    list_display  = ('id', 'cliente', 'valor', 'aliquota', 'iss', 'valor_liq', 'criado_em')
    list_filter   = ('aliquota', 'criado_em')
    search_fields = ('cliente__nome',)