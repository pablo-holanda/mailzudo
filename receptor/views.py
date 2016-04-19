# -*- coding: utf-8 -*-
import mandrill
from .models import Projetos, Submissao, Remetente
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import re
from datetime import datetime

API_KEY = '0HkaXMTUlPa4J-Mfu8Ha2A'


def send_mail(template_name, email_to, nome_remetente, email_remetente):
    mandrill_client = mandrill.Mandrill(API_KEY)
    message = {
        'to': [],
        'global_merge_vars': [],
        'from_email': email_remetente,
        'from_name': nome_remetente,
    }
    try:
        for em in email_to:
            message['to'].append({'email': em})
    except:
        return 1
    # for k, v in context.iteritems():
    #     message['global_merge_vars'].append(
    #         {'name': k, 'content': v}
    #     )
    result = mandrill_client.messages.send_template(template_name, [], message)


@csrf_exempt
def receptor_solicitacoes(request):
    try:
        remetente = json.loads(request.body)
    except:
        return JsonResponse({'status': 'Json invalido!'})

    try:
        usuario_remetente = Projetos.objects.get(usuario__cpf=remetente['cpf'], projeto=remetente['projeto'])

        if not usuario_remetente.usuario.ativo:
            return JsonResponse({'status': 'Usuario sem permissao de envio'})
        elif not usuario_remetente.ativo:
            return JsonResponse({'status': 'Projeto inativo'})

        if type(remetente['para']) != list:
            return JsonResponse({'status': 'Lista de remetentes fora do padrao.'})

        submissao = Submissao(remetente_id=Remetente.objects.get(cpf=remetente['cpf']).pk,
                              projeto_id=Projetos.objects.get(projeto=remetente['projeto']).pk,
                              quantidade_de_emails=len(remetente['para']))

        submissao.save()

        domain = re.search("@[\w.]+", remetente['email_remetente'])

        if domain.group() == '@sedis.ufrn.br':
            mandrill_client = mandrill.Mandrill(API_KEY)
            data = datetime.now().strftime("%d-%m-%Y as %H:%M:%S")
            message = {
                'from_email': 'x9@sedis.ufrn.br',
                'from_name': 'X9 Emails SEDIS',
                'subject': 'Disparo de email SEDIS - Mandrill',
                'text': 'Luide, \n\nO usuário {0} disparou {1} emails no dia {2}.'.format(
                                                        usuario_remetente.usuario.nome, len(remetente['para']), data),
                'to': [{'email': 'luide@sedis.ufrn.br',
                        'name': 'Luide Capanema',
                        'type': 'to'}],
            }
            result = mandrill_client.messages.send(message=message)

        result = send_mail(remetente['template'], remetente['para'], remetente['nome_remetente'],
                           remetente['email_remetente'])

        return JsonResponse({'status': 'enviado'})
    except Projetos.DoesNotExist:
        return JsonResponse({'status': 'Erro desconhecido x('})

