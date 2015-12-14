# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CardValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.PositiveIntegerField(verbose_name=b'\xe4\xbb\xb7\xe5\x80\xbc')),
            ],
            options={
                'verbose_name': '\u6cb9\u5361',
                'verbose_name_plural': '\u6cb9\u5361',
            },
        ),
        migrations.CreateModel(
            name='CoalType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
                'verbose_name': '\u7164\u7c7b\u578b',
                'verbose_name_plural': '\u7164\u7c7b\u578b',
            },
        ),
        migrations.CreateModel(
            name='Mine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('user', models.ForeignKey(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u7164\u77ff',
                'verbose_name_plural': '\u7164\u77ff',
            },
        ),
        migrations.CreateModel(
            name='Scale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('user', models.OneToOneField(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u78c5\u623f',
                'verbose_name_plural': '\u78c5\u623f',
            },
        ),
        migrations.CreateModel(
            name='TransRec',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('car_no', models.CharField(max_length=10)),
                ('driver_name', models.CharField(max_length=10)),
                ('contact_info', models.CharField(max_length=20)),
                ('setoff_time', models.DateTimeField(auto_now_add=True)),
                ('qrcode', models.CharField(max_length=10, unique=True, null=True)),
                ('setoff_amount', models.FloatField(null=True)),
                ('arrive_amount', models.FloatField(null=True)),
                ('arrive_time', models.DateTimeField(null=True)),
                ('cash', models.FloatField(null=True)),
                ('card', models.ForeignKey(to='work.CardValue', null=True)),
                ('coal_type', models.ForeignKey(to='work.CoalType')),
                ('mine', models.ForeignKey(to='work.Mine')),
                ('scale', models.ForeignKey(to='work.Scale', null=True)),
            ],
            options={
                'permissions': (('mine', 'mine'), ('scale', 'scale'), ('account', 'account')),
            },
        ),
    ]
