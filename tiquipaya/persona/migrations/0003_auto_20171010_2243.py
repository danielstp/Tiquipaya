# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 02:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_auto_20171010_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='estadoCivil',
            field=models.ForeignKey(default='Soltero', on_delete=django.db.models.deletion.PROTECT, to='persona.EstadoCivil'),
        ),
    ]
