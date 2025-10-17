from django.core.mail import EmailMessage

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
        'Entre em <a href="https://ferias.macrosul.com/">https://ferias.macrosul.com/</a> e realize a verificação desse pedido.'
        f'{assinatura_html}'
    )

    email = EmailMessage(
        subject='Pedido de Férias',
        body=corpo_html,  # HTML direto como conteúdo principal
        from_email='sistema@macrosul.com',
        to=['rh@macrosul.com'],
        cc=[solicitacao.email_gestor],  # cópia, opcional
    )

    email.content_subtype = "html"  # define o conteúdo como HTML
    email.send()

#EMAIL PARA O COLABORAOR AVISANDO QUE A SOLICITAÇÃO DELE FOI NEGADA
def email_solicitacao_reprovada(solicitacao):
    corpo_html = (
        f'Olá {solicitacao.user}, infelizmente sua solicitação de férias foi recusada. '
        f'O motivo informado pelo RH foi: {solicitacao.motivo_rejeicao}. '
        'Para mais detalhes, entre em contato com o setor de RH.'
        f'{assinatura_html}'
    )

    email = EmailMessage(
        subject='Férias Recusadas',
        body=corpo_html,
        from_email='sistema@macrosul.com',
        to=[solicitacao.user.email],
        cc=[solicitacao.email_gestor],
    )

    email.content_subtype = "html"
    email.send()

#EMAIL PARA O COLABORAOR AVISANDO QUE A SOLICITAÇÃO DELE FOI APROVADA
def email_solicitacao_aprovada(solicitacao):
    inicio_descanso = solicitacao.inicio_do_descanso.strftime("%d/%m/%Y")
    fim_descanso = solicitacao.fim_do_descanso.strftime("%d/%m/%Y")
    corpo_html = (
        f'Olá {solicitacao.user}, sua solicitação de férias no período de {inicio_descanso} até {fim_descanso} foi aprovada! '
        'Aproveite bem suas férias, bom descanso!'
        f'{assinatura_html}'
    )

    email = EmailMessage(
        subject='Férias Aprovadas',
        body=corpo_html,
        from_email='sistema@macrosul.com',
        to=[solicitacao.user.email],
        cc=[solicitacao.email_gestor],
    )

    email.content_subtype = "html"
    email.send()

#EMAIL PARA O COLABORAOR E PARA O RH AVISANDO QUE AS FÉRIAS ESTÃO PRÓXIMAS DO VENCIMENTO
def email_vencimento_proximo(card):
    vencimento_das_ferias = card.data_de_vencimento_de_ferias.strftime("%d/%m/%Y")

    corpo_html_rh = (
        f'Atenção, o(a) colaborador(a) {card.colaborador} está com as férias próximas do vencimento ({vencimento_das_ferias}) '
        f'e ainda possui um saldo de férias de: {card.saldo_de_ferias}. '
        'Por favor, entre em contato para regularizar a situação o mais rápido possível.'
        f'{assinatura_html}'
    )

    email_rh = EmailMessage(
        subject='Vencimento de Férias Próximo',
        body=corpo_html_rh,
        from_email='sistema@macrosul.com',
        to=['rh@macrosul.com'],
    )

    email_rh.content_subtype = "html"
    email_rh.send()

    corpo_html_colaborador = (
        f'Atenção {card.colaborador}, suas férias estão próximas do vencimento ({vencimento_das_ferias}) '
        f'e você ainda possui um saldo de férias de: {card.saldo_de_ferias}. '
        'Por favor, crie uma solicitação de férias em <a href="https://ferias.macrosul.com/">https://ferias.macrosul.com/</a> ou entre em contato com o RH para regularizar a situação o mais rápido possível.'
        f'{assinatura_html}'
    )

    email_colab = EmailMessage(
        subject='Vencimento de Férias Próximo',
        body=corpo_html_colaborador,
        from_email='sistema@macrosul.com',
        to=[card.colaborador.email],
    )

    email_colab.content_subtype = "html"
    email_colab.send()

#EMAIL PARA O COLABORAOR AVISANDO QUE A SUA CONTA FOI CRIADA
def email_colaborador_adicionado(card,senha_aleatoria):
    corpo_html = (
        f'Olá, {card.colaborador}!<br><br>'
        'Informamos que o setor de RH criou sua conta no site <a href="https://ferias.macrosul.com/">https://ferias.macrosul.com/</a>, onde serão realizadas as futuras solicitações de férias. '
        f'Para acessar o sistema pela primeira vez, utilize seu email corporativo da Macrosul e a senha "{senha_aleatoria}". Ou se preferir clique na opção "<strong>Esqueci minha senha</strong>" na tela de login para criar uma nova senha de acesso.<br><br>'
        'A partir de agora, as solicitações de férias deverão ser feitas exclusivamente pelo site, não sendo mais necessário o envio de email ao RH.'
        f'{assinatura_html}'
    )

    email = EmailMessage(
        subject='Conta Criada',
        body=corpo_html,
        from_email='sistema@macrosul.com',
        to=[card.colaborador.email],
    )
    
    email.content_subtype = "html"
    email.send()