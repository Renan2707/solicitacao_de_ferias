from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from core.forms import SolicitacaoDeFeriasForm, VerificaSolicitacaoForm
from core.models.solicitacao import SolicitacaoDeFerias
from core.models.card import Card
from datetime import timedelta, datetime

@login_required
def add_solicitacao(request):
    #MELHORIA: VERIFICAR SE O USUÁRIO JÁ POSSUI UMA SOLICITAÇÃO PENDENTE, FAZER VERIFICAÇÕES AUTOMATICAS COM RELAÇÃO AO SALDO E DATA 
    card_usuario = Card.objects.get(colaborador=request.user)
    if request.method == 'POST':
        form = SolicitacaoDeFeriasForm(request.POST, request.FILES)
        if form.is_valid():
            solicitacao = form.save(commit=False)
            solicitacao.card = card_usuario
            solicitacao.user = request.user
            solicitacao.fim_do_descanso = form.cleaned_data['inicio_do_descanso'] + timedelta(days=int(form.cleaned_data['dias_de_descanso']))
            solicitacao.save()
            return render(request, 'core/index.html', {'form': form,'success': True })
        else:
            return render(request, 'core/index.html', {'form': form, 'form_errors': form.errors})
    else:
        form = SolicitacaoDeFeriasForm()
        return render(request, 'core/index.html', {'form': form})
    

@login_required
def reprovar_solicitacao(request, id_solicitacao):
    solicitacao = SolicitacaoDeFerias.objects.get(pk=id_solicitacao)
    solicitacao.ferias_rejeitadas = True
    solicitacao.save()
    return redirect(reverse('index'))

@login_required
def aprovar_solicitacao(request, id_solicitacao):
    solicitacao = SolicitacaoDeFerias.objects.get(pk=id_solicitacao)

    if request.method == 'POST':
        form = VerificaSolicitacaoForm(request.POST)
        if form.is_valid():
            #APROVANDO A SOLICITAÇÃO
            solicitacao.solicitacao_aprovada = True
            #ATUALIZANDO O SALDO DO CARD
            saldo = int( solicitacao.card.saldo_de_ferias)
            dias_descanso_solicitados = int(solicitacao.dias_de_descanso)
            dias_venda_solicitados = int(solicitacao.dias_vendidos)
            dias_totais_solicitados = dias_descanso_solicitados + dias_venda_solicitados
            solicitacao.card.saldo_de_ferias = saldo - dias_totais_solicitados
            #SALVANDO CARD E SOLICITACAO
            solicitacao.save()
            solicitacao.card.save()
            #VERIFICANDO SE AS FÉRIAS JÁ PODEM SER INICIADAS
            verificar_inicio_das_ferias()
            return redirect(reverse('index'))
        else:
            return render(request, 'core/index.html', {'form': form, 'form_errors': form.errors})
    return redirect(reverse('index'))


def verificar_inicio_das_ferias():
    solicitacoes = SolicitacaoDeFerias.objects.filter(solicitacao_aprovada=True)
    for solicitacao in solicitacoes:
        if solicitacao.inicio_do_descanso <= datetime.now().date() and not solicitacao.ferias_iniciadas:
            solicitacao.ferias_iniciadas = True
            solicitacao.save()
    return redirect(reverse('index'))



def verificar_fim_das_ferias(request):
    solicitacoes = SolicitacaoDeFerias.objects.filter(ferias_iniciadas=True)
    for solicitacao in solicitacoes:
        if solicitacao.fim_do_descanso <= datetime.now().date():
            solicitacao.ferias_finalizadas = True
            solicitacao.save()
    return redirect(reverse('index'))    


