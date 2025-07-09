from django.db import models
from django.contrib.auth.models import User
from core.models.card import Card

class SolicitacaoDeFerias(models.Model):
    dias_de_descanso = models.CharField(blank=False, null=False)
    dias_vendidos = models.CharField(blank=False, null=False)
    email_gestor= models.CharField(blank=False, null=False)
    email_colaborador = models.CharField(blank=False, null=False)
    nome_colaborador = models.CharField( blank=False, null=False)
    card = models.ForeignKey(Card, blank=True, null=True, on_delete=models.CASCADE, related_name='solicitacoes_de_ferias')
    
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_colaborador
    
    class Meta:
        verbose_name = "Solicitacao De Ferias"
        verbose_name_plural = "Solicitacões De Ferias"
      