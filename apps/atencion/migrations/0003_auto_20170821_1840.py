# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 23:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atencion', '0002_auto_20170804_1702'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='atencioncontrol',
            options={'ordering': ('pk',)},
        ),
    ]
