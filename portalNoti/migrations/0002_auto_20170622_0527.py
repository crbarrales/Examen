# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 05:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portalNoti', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='sort_order',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='sort_order',
        ),
    ]