from django.db import models
from django.contrib.auth.models import User

class Card(models.Model):
    setor = models.CharField()
    data_de_admissao = models.CharField(blank=False, null=False)
    data_de_vencimento_de_ferias= models.CharField(blank=False, null=False)
    saldo_de_ferias = models.CharField(blank=False, null=False)
    colaborador = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='cards')
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.colaborador
    class Meta:
        verbose_name = "Card"
        verbose_name_plural = "Cards"
        