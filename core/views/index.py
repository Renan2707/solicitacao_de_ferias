from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from rolepermissions.roles import assign_role
from core.models.card import Card
from core.models.solicitacao import SolicitacaoDeFerias

@login_required
def index(request):
    cards = Card.objects.all()
    solicitacoes = SolicitacaoDeFerias.objects.all()
    return render(request, 'core/index.html', {'cards': cards, 'solicitacoes': solicitacoes})

def criar_user_rh(request):
    user = User.objects.create_user(
        username='renan_rh',
        password='RE0101si@')
    user.save()
    assign_role(user, 'rh')
    return HttpResponse("Usuário RH criado com sucesso!")   