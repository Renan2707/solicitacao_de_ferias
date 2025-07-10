from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from core.forms import SolicitacaoDeFeriasForm
from core.models.card import Card

@login_required
def add_solicitacao(request):
    card_usuario = Card.objects.get(colaborador=request.user)
    if request.method == 'POST':
        form = SolicitacaoDeFeriasForm(request.POST, request.FILES)
        if form.is_valid():
            solicitacao = form.save(commit=False)
            solicitacao.card = card_usuario
            solicitacao.user = request.user
            solicitacao.save()
            return render(request, 'core/index.html', {'form': form,'success': True })
        else:
            return render(request, 'core/index.html', {'form': form, 'form_errors': form.errors})
    else:
        form = SolicitacaoDeFeriasForm()
        return render(request, 'core/index.html', {'form': form})