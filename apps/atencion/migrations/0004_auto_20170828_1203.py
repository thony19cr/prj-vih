# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atencion', '0003_auto_20170821_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='triaje',
            name='imc',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='IMC'),
        ),
    ]
