import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'solicitacao_de_ferias.settings')

app = Celery('solicitacao_de_ferias')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def verifica_solicitacoes(self):
    from core.views.cards import vencimento_proximo
    vencimento_proximo()

    from core.views.solicitacao import verificar_inicio_das_ferias
    verificar_inicio_das_ferias()

    from core.views.cards import renova_saldo_de_ferias
    renova_saldo_de_ferias()

    from core.views.solicitacao import verificar_fim_das_ferias
    verificar_fim_das_ferias()