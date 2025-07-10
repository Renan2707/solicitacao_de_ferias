from django.urls import path
from core.views.cards import add_colaborador, vencimento_proximo

urlpatterns = [
   path('add_colaborador/', add_colaborador, name='add_colaborador'),
   path('vencimento_proximo/', vencimento_proximo, name='vencimento_proximo'),
]