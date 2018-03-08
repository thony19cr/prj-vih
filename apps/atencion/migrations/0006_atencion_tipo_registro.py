# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 23:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atencion', '0005_auto_20170920_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='atencion',
            name='tipo_registro',
            field=models.CharField(blank=True, choices=[('WEB', 'VIH'), ('MOVIL', 'APP_VIH')], max_length=5, null=True),
        ),
    ]
