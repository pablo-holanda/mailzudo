# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 21:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('receptor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.FileField(upload_to='imagens/')),
                ('descricao', models.CharField(blank=True, max_length=120)),
                ('image_url', models.URLField(blank=True)),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receptor.Projetos')),
            ],
        ),
    ]
