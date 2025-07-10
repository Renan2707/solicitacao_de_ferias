from django.db import models
from django.contrib.auth.models import User

class Card(models.Model):
    setor = models.CharField()
    nome = models.CharField(blank=True, null=True)
    email = models.CharField(blank=True, null=True)
    data_de_admissao = models.DateTimeField(blank=False, null=False)
    data_de_vencimento_de_ferias= models.DateTimeField(blank=False, null=False)
    saldo_de_ferias = models.CharField(blank=False, null=False)
    colaborador = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='cards')
    data_de_vencimento_proxima = models.BooleanField(default=False)
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Card"
        verbose_name_plural = "Cards"
        