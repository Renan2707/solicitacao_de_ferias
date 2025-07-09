from django.contrib import admin

from core.models.solicitacao import SolicitacaoDeFerias
from core.models.card import Card

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('setor', 'data_de_admissao', 'data_de_vencimento_de_ferias', 'saldo_de_ferias', 'colaborador', 'criado_em', 'atualizado_em')
    search_fields = ('setor', 'colaborador__username')
    list_filter = ('setor',)
    ordering = ('-criado_em',)

@admin.register(SolicitacaoDeFerias)
class SolicitacaoDeFeriasAdmin(admin.ModelAdmin):
    list_display = ('nome_colaborador', 'dias_de_descanso', 'dias_vendidos', 'email_gestor', 'email_colaborador', 'card', 'criado_em')
    search_fields = ('nome_colaborador', 'email_gestor', 'email_colaborador')
    list_filter = ('card__setor',)
    ordering = ('-criado_em',)
