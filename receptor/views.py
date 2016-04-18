# -*- coding: utf-8 -*-
from django.shortcuts import render
import mandrill
from .models import Remetente, Projetos
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



API_KEY = '0HwTCmZKlB4a4pewH8NysA'


def send_mail(template_name, email_to):
    mandrill_client = mandrill.Mandrill(API_KEY)
    message = {
        'to': [],
        'global_merge_vars': []
    }
    for em in email_to:
        message['to'].append({'email': em})

    # for k, v in context.iteritems():
    #     message['global_merge_vars'].append(
    #         {'name': k, 'content': v}
    #     )
    mandrill_client.messages.send_template(template_name, [], message)


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



        return JsonResponse({'status': 'enviado'})
    except Projetos.DoesNotExist:
        return JsonResponse({'status': 'Erro desconhecido x('})

