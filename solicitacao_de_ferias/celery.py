import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'solicitacao_de_ferias.settings')

app = Celery('solicitacao_de_ferias')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Hello from celery')


@app.task(bind=True)
def hello(self):
    print('Hello 2')
