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

    def clean_inicio_do_descanso(self):
        inicio = self.cleaned_data["inicio_do_descanso"]
        # date.weekday(): 0=segunda … 3=quinta, 4=sexta
        if inicio.weekday() in (3, 4, 5, 6):
            raise forms.ValidationError(
                "O início do descanso não pode ser quinta‑feira, sexta‑feira ou em fins de semana."
            )
        return inicio

class VerificaSolicitacaoForm(forms.Form):
    saldo_de_ferias_necessario =  forms.BooleanField(required=True)
    quantidade_de_dias_para_venda =  forms.BooleanField(required=True)
    data_de_solicitacao_valida =  forms.BooleanField(required=True)
    comunicou_o_gestor = forms.BooleanField(required=True)
    aprovado_pela_diretoria = forms.BooleanField(required=True)
