# -*- coding: utf-8 -*-
import mandrill


lista_lais = ["custodioguerra@yahoo.com.br ", "danilo.nagem@gmail.com ", "hertzw@gmail.com ", "lyaneramalho@gmail.com ",
         "higormorais@gmail.com ", "philippi.sedir@gmail.com ", "monte.daniele@gmail.com ", "jailtoncarlos@gmail.com ",
         "ribeirodantasdm@gmail.com ", "aquilesburlamaqui@gmail.com ", "allysonbarrosrn@gmail.com ",
         "rraffaelpinto@gmail.com ", "rdsilva0205@gmail.com ", "robinson.alves25@gmail.com ", "paivatulio@gmail.com ",
         "janioguga@gmail.com ", "karilany@gmail.com ", "kakayzinha@gmail.com ", "marcellofs777@gmail.com ",
         "alinepinhodias@gmail.com ", "janaina.lrsv@gmail.com ", "heloisalemos05@gmail.com ", "hekis1963@gmail.com ",
         "idelmarcia@gmail.com ", "brunogomes3000@gmail.com ", "joao.queiroz@lais.huol.ufrn.br ",
         "cinthiadahora@gmail.com ", "kaline@sedis.ufrn.br ", "mauriciojornalista@gmail.com ", "caoeduc@gmail.com ",
         "pedrotrv.lais@gmail.com ", "milenaduartea@gmail.com ", "karlamonica@hotmail.com ",
         "lawrencemedeiros89@gmail.com", "brunolinhares25000@gmail.com", "giveldnap@gmail.com",
         "geir_veras@hotmail.com", "lucascassiano21@gmail.com", "natanaelfneto@outlook.com", "thalescast@gmail.com",
         "paulovictorguerra@gmail.com", "dayallamarques@gmail.com", "nicole.alves@lais.huol.ufrn.br",
         "nicolasvinicius77@gmail.com", "camila.regia2007@hotmail.com", "isabelemagaldi@gmail.com",
         "cefas.rodrigues04@gmail.com", "mateus.gabriel182@outlook.com", "edwilliam_araujo@hotmail.com",
         "hugogsoaresfontes@gmail.com", "luis_felipe_soares@hotmail.com", "renata-araujo11@hotmail.com",
         "rayanodb@gmail.com", "jvictorcabral@hotmail.com", "phol4nda@gmail.com", "yaskaramenescal@gmail.com",
         "vinicius_lima_1@hotmail.com", "victormatheuscastro@gmail.com", "galvaoazevedod@gmail.com"]


jornalistas = ["agnelof@terra.com.br", "anaruth@tribunadonorte.com.br", "antonioroberto@tribunadonorte.com.br", "cpeditor@digizap.com.br", "cadernoviver@tribunadonorte.com.br", "cledivania@tribunadonorte.com.br", "elianalima@tribunadonorte.com.br", "hilnethcorreia@tribunadonorte.com.br", "hudson@tribunadonorte.com.br", "esporte@tribunadonorte.com.br", "jrac.nat@terra.com.br", "liegebarbalho@tribunadonorte.com.br,liegebarbalho@uol.com.br", "laf@tribunadonorte.com.br", "renatamoura@tribunadonorte.com.br", "rlalves.nat@terra.com.br", "colunasnotas@tribunadonorte.com.br", "angelicahipolito@uol.com.br,angelicahipolito@tvpontanegra.com.br", "claudiaangelica@pop.com.br", "cr.is.lu@hotmail.com", "cristianemacedo@yahoo.com.br", "cirorobson@hotmail.com", "danielcabral@tvpontanegra.com.br", "inamarjornalista@gmail.com", "jacson_d@hotmail.com", "ferreiravitor92@hotmail.com", "luishenriquenatal@gmail.com", "gutho@tvpontanegra.com.br", "lopesrn@hotmail.com", "producao1980@yahoo.com.br", "aluizio.neto@redeintertv.com.br", "antonio.araujo@redintertv.com.br", "diana.barreto@redeintertv.com.br", "dirceu.simabucuru@redeintertv.com.br", "francisco.junior@redeintertv.com.br", "lidia.pace@redeintertv.com.br", "liziane.virgilio@redeintertv.com.br", "ludmilla.lacerda@redeintertv.com.br", "luiz.alberto@redeintertv.com.br", "marcia.elisa@redeintertv.com.br", "michelle.rincon@redeintertv.com.br", "murilo.meireles@redeintertv.com.br", "thiago.cesar@redeintertv.com.br", "kleberjornalismo@hotmail.com", "mara.godeiro@redeintertv.com.br", "janiovidal@uol.com.br", "rafaelcruz@redetropical.com.br", "medeiros_cristiano@hotmail.com", "rodrigo_sloureiro@gmail.com,", "contato@rodrigoloureiro.com.br", "bruno@blogdobg.com.br", "simonesilvarn1@gmail.com,", "sim,eventosrn@gmail.com", "lira_cris@hotmail.com,cristinalira@ig.com.br,cristinalira80@gmail.com", "lauritaarruda@gmail.com", "thaisagalvao@gmail.com", "fotografia@canindesoares.com", "ricardo@fazpro.com.br", "rosaliearruda@uol.com.br", "chrystiandesaboya@digizap.com.br", "ianoflavio@tvu.ufrn.br", "superint@comunica.ufrn.br", "comercial2@radiocidadenatal.com.br", "helainearocha@gmail.com", "zeeudo@hotmail.com", "rosemiltonsilva@carroecampo.com.br", "eniosinedino@96fm.com.br", "felintof@radio98.fm.br", "robsonvcarvalho@hotmail.com", "asoares@band.com.br", "firodrigues@band.com.br", "ldayana@band.com.br", "mleiros@band.com.br", "mpaula@band.com.br", "ilana@portalnoar.com", "bw.araujo@gmail.com", "julio@portalnoar.com", "kellybarrostv@gmail.com", "allandarlyson@hotmail.com", "dinarteassuncao@gmail.com", "mlima2001@yahoo.com.br", "vmdfranca@gmail.com", "saullotarso@yahoo.com.br", "diogenes@blogdodiogenes.com.br;", "diogenes@nominuto.com", "edmosinedino@gmail.com", "gerlaneoliv@hotmail.com;", "gerlane@nominuto.com", "robertoguedes@nominuto.com", "rtblau@bol.com.br", "tgo_medeiros@hotmail.com", "argemirolima@novojornal.jor.br", "augustobezerril@novojornal.jor.br", "carlosmagno@novojornal.jor.br", "cassiano@novojornal.jor.br;", "cassianoarruda@novojornal.jor.br;rodaviva@novojornal.jor.br", "evertondantas@novojornal.jor.br", "iraniltonmarcolino3@gmail.com", "louiseaguiar@novojornal.jor.br", "luanxavier.rn@gmail.com", "marcosbezerra@novojornal.jor.br", "sadepaula@novojornal.jor.br", "mouraneto@novojornal.jor.br", "rafaelduarte@novojornal.jor.br", "renato.sumatra@gmail.com", "silvioandrade@novojornal.jor.br", "viktorvidal@novojornal.jor.br", "marinesfornaciari@yahoo.com.br", "virginia@muitasoutras.com.br", "miguelweber@bol.com.br", "eniosinedino@96fm.com.br", "suzanamenezes@96fm.com.br", "felintof@radio98.fm.br", "robsonvcarvalho@hotmail.com"]

API_KEY = '0HkaXMTUlPa4J-Mfu8Ha2A'
# mandrill_client = mandrill.Mandrill(API_KEY)
#
# for email in lista:
#     message = {
#                'from_email': 'avasus@lais.huol.ufrn.br',
#                'from_name': 'AVASUS',
#                'subject': 'Não divulgar sobre o AVASUS',
#                'tags': ['email normal'],
#                'text': 'Pessoal, peço que não divulguem o AVASUS até as 17:00Hrs de amanhã. \n\n O email anterior foi apenas uma divulgação interna entre os integrantes do LAIS, em sua maioria pesquisadores e coordenadores de projetos, que serviu para testar nossa nova API de email. \n\n Conto com a compreensão de todos.',
#                'to': [{'email': email}],
#                 }
#
#
#     result = mandrill_client.messages.send(message=message)
#     print result

# def send_mail(template_name, email_to):
#     mandrill_client = mandrill.Mandrill(API_KEY)
#     message = {
#         'to': [],
#         'global_merge_vars': []
#     }
#     for em in email_to:
#         message['to'].append({'email': em})
#
#     # for k, v in context.iteritems():
#     #     message['global_merge_vars'].append(
#     #         {'name': k, 'content': v}
#     #     )
#     # resposta = mandrill_client.messages.send_template(template_name, [], message)
#
#     algo = mandrill_client.messages.send(message)
#
#     print algo
#
#
# send_mail('Grupo2 AVASUS', 'phol4nda@gmail.com')
