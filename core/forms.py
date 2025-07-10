from core.models.card import Card
from core.models.solicitacao import SolicitacaoDeFerias
from django import forms

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['setor', 'data_de_admissao', 'data_de_vencimento_de_ferias', 'saldo_de_ferias', 'colaborador','nome', 'email']


class SolicitacaoDeFeriasForm(forms.ModelForm):
    class Meta:
        model = SolicitacaoDeFerias
        fields = ['user','dias_de_descanso', 'dias_vendidos', 'email_gestor', 'inicio_do_descanso', 'observacao_do_gestor', 'comunicacao_com_gestor', 'card','fim_do_descanso', 'solicitacao_aprovada', 'ferias_iniciadas', 'ferias_finalizadas', 'ferias_rejeitadas']