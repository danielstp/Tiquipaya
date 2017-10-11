# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 02:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='estadoCivil',
            field=models.ForeignKey(default='Soltero', on_delete=django.db.models.deletion.PROTECT, to='persona.EstadoCivil'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='persona',
            name='sexo',
            field=models.ForeignKey(default='Femenino', on_delete=django.db.models.deletion.PROTECT, to='persona.Sexo'),
        ),
    ]
