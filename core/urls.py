from django.urls import path
from core.views.cards import add_colaborador, vencimento_proximo

from core.views.solicitacao import add_solicitacao, reprovar_solicitacao, aprovar_solicitacao, verificar_fim_das_ferias

urlpatterns = [
   path('add_colaborador/', add_colaborador, name='add_colaborador'),
   path('vencimento_proximo/', vencimento_proximo, name='vencimento_proximo'),
   path('add_solicitacao/', add_solicitacao, name='add_solicitacao'),
   path('reprovar_solicitacao/<str:id_solicitacao>/', reprovar_solicitacao, name='reprovar_solicitacao'),
   path('aprovar_solicitacao/<str:id_solicitacao>/', aprovar_solicitacao, name='aprovar_solicitacao'),
   path('verificar_fim_das_ferias/', verificar_fim_das_ferias, name='verificar_fim_das_ferias'),
]