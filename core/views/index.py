from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from rolepermissions.roles import assign_role
from core.models.card import Card
from core.models.solicitacao import SolicitacaoDeFerias

@login_required
def index(request):
    query = request.GET.get('pesquisa')  # Pegando o termo pesquisado
    if query:
        cards = Card.objects.filter(colaborador__username__icontains=query)
        solicitacoes = SolicitacaoDeFerias.objects.filter(user__username__icontains=query)
    else:
        cards = Card.objects.all()
        solicitacoes = SolicitacaoDeFerias.objects.all()
        query = ''
    return render(request, 'core/index.html', {
        'cards': cards,
        'solicitacoes': solicitacoes,
        'query': query  # para manter o valor no input da barra de busca
    })

def criar_user_rh(request):
    user = User.objects.create_user(
        username='renan_rh',
        password='RE0101si@')
    user.save()
    assign_role(user, 'rh')
    return HttpResponse("Usuário RH criado com sucesso!")   

@login_required
def historico_rh(request):
    cards = Card.objects.all()
    if request.method == 'GET':
        solicitacoes = SolicitacaoDeFerias.objects.all()
        return render(request, 'core/sections/historico_rh.html', {'cards': cards, 'solicitacoes': solicitacoes})
    else:
        tipo_filtro = request.POST.get('tipo_filtro')
        filtro_colaborador = request.POST.get('filtro_colaborador')
        filtro_status = request.POST.get('filtro_status')

        if filtro_colaborador:
            solicitacoes = SolicitacaoDeFerias.objects.filter(user__username = filtro_colaborador)

        elif tipo_filtro == 'status':
            if filtro_status == 'recusada':
                solicitacoes = SolicitacaoDeFerias.objects.filter(ferias_rejeitadas = True)

            elif filtro_status == 'em-aberto':
                solicitacoes = SolicitacaoDeFerias.objects.filter(solicitacao_aprovada = False, ferias_rejeitadas = False)

            elif filtro_status == 'aprovada':
                solicitacoes = SolicitacaoDeFerias.objects.filter(solicitacao_aprovada = True, ferias_iniciadas = False)

            elif filtro_status == 'finalizada':
                solicitacoes = SolicitacaoDeFerias.objects.filter(ferias_finalizadas = True)

            elif filtro_status == 'em-ferias':
                solicitacoes = SolicitacaoDeFerias.objects.filter(ferias_iniciadas = True, ferias_finalizadas = False)
            else:
                solicitacoes = SolicitacaoDeFerias.objects.all()
        else:
            solicitacoes = SolicitacaoDeFerias.objects.all()
            
        return render(request, 'core/sections/historico_rh.html', {'cards': cards, 'solicitacoes': solicitacoes})
