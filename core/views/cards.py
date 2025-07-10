from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from core.forms import CardForm
from core.models.card import Card
from datetime import datetime
from django.contrib import messages

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
            messages.success(request, 'Colaborador adicionado com sucesso!')
            return redirect(reverse('index'))
        else:
            messages.error(request, 'Erro ao adicionar colaborador. Verifique os dados informados.')
            return redirect(reverse('index'))
    
    else:
        form = CardForm()
        return render(request, 'core/index.html', {'form': form,'cards': cards})
    

def vencimento_proximo(request):
    cards = Card.objects.all()
    hoje = datetime.now().date()
    for card in cards:
        data_venc = card.data_de_vencimento_de_ferias
        if isinstance(data_venc, datetime):
            data_venc = data_venc.date()
        if data_venc <= hoje:
            card.data_de_vencimento_proxima = True
        else:
            card.data_de_vencimento_proxima = False
        card.save()
    return redirect(reverse('index'))