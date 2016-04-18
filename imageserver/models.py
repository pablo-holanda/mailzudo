from __future__ import unicode_literals

from django.db import models
from receptor.models import Projetos


class Imagens(models.Model):
    imagem = models.FileField(upload_to='imagens/')
    projeto = models.ForeignKey(Projetos)
    descricao = models.CharField(max_length=120, blank=True)
    image_url = models.URLField(blank=True)

    def save(self):
        super(Imagens, self).save()
        self.image_url = self.imagem.url
        super(Imagens, self).save()

    def __unicode__(self):
        return '%s' % self.descricao
