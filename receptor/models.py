# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Remetente(models.Model):
    nome = models.CharField(max_length=60)
    ativo = models.BooleanField(default=True)
    cpf = models.CharField(max_length=15, unique=True)

    def __unicode__(self):
        return '%s' % self.nome


class Projetos(models.Model):
    usuario = models.ForeignKey(Remetente)
    projeto = models.CharField(max_length=120)
    ativo = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s' % self.projeto

    class Meta:
        verbose_name = u'Projeto'
        verbose_name_plural = u'Projetos'


class Submissao(models.Model):
    remetente = models.ForeignKey(Remetente)
    projeto = models.ForeignKey(Projetos)
    data_de_envio = models.DateTimeField(auto_now_add=True, blank=True)
    quantidade_de_emails = models.IntegerField()

    def __unicode__(self):
        return 'Remetente: %s | Emails: %d | Data: %s' % (self.remetente, self.quantidade_de_emails,
                                                          self.data_de_envio.strftime("%d-%m-%Y %H:%M:%S"))

    class Meta:
        verbose_name = u'Submissão'
        verbose_name_plural = u'Submissões'