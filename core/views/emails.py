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



#EMAIL PARA O COLABORAOR E PARA O RH AVISANDO QUE AS FÉRIAS ESTÃO PRÓXIMAS DO VENCIMENTO
def email_vencimento_proximo(card):
    corpo_html_rh = (
        f'Atenção, o(a) colaborador(a) {card.colaborador} está com as férias próximo do vencimento ({card.data_de_vencimento_de_ferias}) e ainda possui um saldo de férias de: {card.saldo_de_ferias}.'
        ' Por favor, entre em contato para regularizar a situação o mais rápido possível.'
        f'{assinatura_html}'
    )
    send_mail(
        'Vencimento de Férias Próximo',
        f'Atenção, o(a) colaborador(a) {card.colaborador} está com as férias próximo do vencimento ({card.data_de_vencimento_de_ferias}) e ainda possui um saldo de férias de: {card.saldo_de_ferias}. Por favor, entre em contato com o(a) colaborador(a) para regularizar a situação o mais rápido possível.',
        'sistema@macrosul.com',
        ['renan.silveira@macrosul.com'],
        html_message=corpo_html_rh
    )

    corpo_html_colaborador = (
        f'Atenção {card.colaborador} suas férias estão próximas do vencimento ({card.data_de_vencimento_de_ferias}) e você ainda possui um saldo de férias de: {card.saldo_de_ferias}.'
        '  Por favor, crie uma solicitação de férias em www.sitedeferias.com.br ou entre em contato com o RH para regularizar a situação o mais rápido possível.'
        f'{assinatura_html}'
    )

    send_mail(
        'Vencimento de Férias Próximo',
        f'Atenção {card.colaborador} suas férias estão próximas do vencimento ({card.data_de_vencimento_de_ferias}) e você ainda possui um saldo de férias de: {card.saldo_de_ferias}. Por favor, crie uma solicitação de férias em www.sitedeferias.com.br ou entre em contato com o RH para regularizar a situação o mais rápido possível.',
        'sistema@macrosul.com',
        [card.colaborador.email],
        html_message=corpo_html_colaborador
    )





#EMAIL PARA O COLABORAOR AVISANDO QUE A SUA CONTA FOI CRIADA
def email_colaborador_adicionado(card):
    corpo_html = (
        f'Olá, {card.colaborador}! Informamos que o setor de RH criou sua conta no site www.sitedasferias.com.br, onde serão realizadas as futuras solicitações de férias. Para acessar o sistema pela primeira vez, utilize seu email corporativo da Macrosul e clique na opção "Esqueci minha senha" na tela de login para criar uma nova senha de acesso. A partir de agora, as solicitações de férias deverão ser feitas exclusivamente pelo site, não sendo mais necessário o envio de email ao RH.'
        f'{assinatura_html}'
    )
    send_mail(
        'Férias Aprovadas',
        f'Olá, {card.colaborador}! Informamos que o setor de RH criou sua conta no site www.sitedasferias.com.br, onde serão realizadas as futuras solicitações de férias. Para acessar o sistema pela primeira vez, utilize seu email corporativo da Macrosul e clique na opção "Esqueci minha senha" na tela de login para criar uma nova senha de acesso. A partir de agora, as solicitações de férias deverão ser feitas exclusivamente pelo site, não sendo mais necessário o envio de email ao RH.',
        'sistema@macrosul.com',
        [card.colaborador.email],
        html_message=corpo_html
    )