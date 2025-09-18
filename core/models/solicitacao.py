from django.db import models
from django.contrib.auth.models import User
from core.models.card import Card

class SolicitacaoDeFerias(models.Model):
    #CAMPOS PREENCHIDOS PELO COLABORADOR:
    dias_de_descanso = models.CharField(blank=False, null=False)
    dias_vendidos = models.CharField(blank=False, null=False)
    email_gestor= models.CharField(blank=False, null=False)
    inicio_do_descanso = models.DateField(blank=False, null=True)
    observacao_do_gestor= models.CharField(blank=True, null=True)
    comunicacao_com_gestor = models.FileField(upload_to='media/',blank=True, null=True)

    # CAMPOS PREENCHIDOS AUTOMATICAMENTE OU NAS VERIFICAÇÕES:
    user= models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE,)
    fim_do_descanso = models.DateField(blank=True, null=True)
    solicitacao_aprovada = models.BooleanField(default=False)
    ferias_iniciadas = models.BooleanField(default=False)
    ferias_finalizadas = models.BooleanField(default=False)
    ferias_rejeitadas = models.BooleanField(default=False)
    card = models.ForeignKey(Card, blank=True, null=True, on_delete=models.CASCADE, related_name='solicitacoes_de_ferias')
    criado_em = models.DateTimeField(auto_now_add=True)

    #CAMPO PREENCHIDO PELO RH:
    motivo_rejeicao = models.CharField(blank=True, null=True, max_length=512)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = "Solicitacao De Ferias"
        verbose_name_plural = "Solicitacões De Ferias"
        ordering = ['-criado_em']  
     
      