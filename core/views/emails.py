from django.core.mail import send_mail

assinatura_html = """
<br><br>
<p>Atenciosamente,<br>
<b>RH Macrosul</b><br>
<br><br>
<img src="https://s3.sa-east-1.amazonaws.com/macrosul.media/itens/viagens-macrosul/imagens-viagem/imagens-viagem-128-1020.png" alt="Macrosul" width="500">
</p>
"""

#EMAIL PARA O RH AVISANDO QUE HÁ UMA NOVA SOLICITAÇÃO
def email_nova_solicitacao(solicitacao):
    corpo_html = (
        f'Olá, o colaborador(a) {solicitacao.user} criou uma nova solicitação de férias. '
        'Entre em www.sitedeferias.com.br e realize a verificação desse pedido.'
        f'{assinatura_html}'
    )
    send_mail(
        'Pedido de Férias',
        f'Olá, o colaborador(a) {solicitacao.user} criou uma nova solicitação de férias. Entre em www.sitedeferias.com.br e realize a verificação desse pedido.',
        'sistema@macrosul.com',
        ['renan.silveira@macrosul.com'],
        html_message=corpo_html
    )



#EMAIL PARA O COLABORAOR AVISANDO QUE A SOLICITAÇÃO DELE FOI NEGADA
def email_solicitacao_reprovada(solicitacao):
    corpo_html = (
        f'Olá, infelizmente sua solicitação de férias foi recusada. '
        'Para mais detalhes, entre em contato com o setor de RH.'
        f'{assinatura_html}'
    )
    send_mail(
        'Férias Recusadas',
        f'Olá, infelizmente sua solicitação de férias foi recusada. Para mais detalhes, entre em contato com o setor de RH.',
        'sistema@macrosul.com',
        [solicitacao.user.email],
        html_message=corpo_html
    )



#EMAIL PARA O COLABORAOR AVISANDO QUE A SOLICITAÇÃO DELE FOI APROVADA
def email_solicitacao_aprovada(solicitacao):
    corpo_html = (
        f'Olá, sua solicitação de férias no perído de {solicitacao.inicio_do_descanso} até {solicitacao.fim_do_descanso} foi aprovada! '
        'Aproveite bem suas férias, bom descanso!'
        f'{assinatura_html}'
    )
    send_mail(
        'Férias Aprovadas',
        f'Olá, sua solicitação de férias no perído de {solicitacao.inicio_do_descanso} até {solicitacao.fim_do_descanso} foi aprovada! Aproveite bem suas férias, bom descanso! ',
        'sistema@macrosul.com',
        [solicitacao.user.email],
        html_message=corpo_html
    )