# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 12:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0004_auto_20151229_0024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scale',
            name='out_unit',
        ),
    ]
