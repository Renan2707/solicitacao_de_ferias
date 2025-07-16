from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from core.forms import CardForm
from core.models.card import Card
from django.contrib import messages
from datetime import timedelta, datetime
from core.models.solicitacao import SolicitacaoDeFerias
from core.views.emails import email_vencimento_proximo, email_colaborador_adicionado


@login_required
def add_colaborador(request):
    cards = Card.objects.all()
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['nome'],
            password='M@crosul2025',
            email=form.cleaned_data['email'])
            user.save()
            card = form.save(commit=False)
            card.colaborador = user
            card.save()
            email_colaborador_adicionado(card)
            messages.success(request, 'Colaborador adicionado com sucesso!')
            return redirect(reverse('index'))
        else:
            messages.error(request, 'Erro ao adicionar colaborador. Verifique os dados informados.')
            return redirect(reverse('index'))
    
    else:
        form = CardForm()
        return render(request, 'core/index.html', {'form': form,'cards': cards})
    

def edit_colaborador(request, id_colaborador):
    card = Card.objects.get(pk=id_colaborador)
    user = card.colaborador
    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            # Atualiza os dados do usuário
            user.username = form.cleaned_data['nome']
            user.email = form.cleaned_data['email']
            user.save()
            card.colaborador = user
            card.save()
            form.save()
            messages.success(request, 'Colaborador editado com sucesso!')
            return redirect(reverse('index'))
        else:
            messages.error(request, 'Erro ao editar colaborador. Verifique os dados informados.')
            return redirect(reverse('index'))
    
def remove_colaborador(request, id_colaborador):
    card = Card.objects.get(pk=id_colaborador)
    solicitacoes = SolicitacaoDeFerias.objects.filter(user=card.colaborador)
    user = card.colaborador
    if request.method == 'POST':
        solicitacoes.delete()
        card.delete()
        user.delete()
        messages.success(request, 'Colaborador removido com sucesso!')
        return redirect(reverse('index'))



def vencimento_proximo(request):
    cards = Card.objects.all()
    hoje = datetime.now().date()
    for card in cards:
        data_venc = card.data_de_vencimento_de_ferias
        if isinstance(data_venc, datetime):
            data_venc = data_venc.date()
        if data_venc <= hoje + timedelta(days=90) and int(card.saldo_de_ferias) > 0:
            card.data_de_vencimento_proxima = True
            email_vencimento_proximo(card)
        else:
            card.data_de_vencimento_proxima = False
        card.save()
    return redirect(reverse('index'))
 

def renova_saldo_de_ferias(request):
    #MELHORIA: VERIFICAR SE O SALDO ESTAVA ZERADO E SE NÃO ESTIVER AVISAR POR EMAIL
    cards = Card.objects.all()
    hoje = datetime.now().date()
    for card in cards:
        data_venc = card.data_de_vencimento_de_ferias
        if isinstance(data_venc, datetime):
            data_venc = data_venc.date()
        if data_venc <= hoje:
            card.saldo_de_ferias = 30
            card.data_de_vencimento_de_ferias = hoje + timedelta(days=365)
        card.data_de_vencimento_proxima = False
        card.save()
    return redirect(reverse('index'))