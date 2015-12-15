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
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.PositiveIntegerField(verbose_name=b'\xe4\xbb\xb7\xe5\x80\xbc')),
                ('balance', models.PositiveIntegerField(default=0, verbose_name=b'\xe4\xbd\x99\xe9\x87\x8f')),
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
            name='Shipment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit', models.FloatField(verbose_name=b'\xe8\xbf\x90\xe8\xb4\xb9\xe5\x8d\x95\xe4\xbb\xb7')),
                ('coal_type', models.ForeignKey(verbose_name=b'\xe7\x85\xa4\xe7\xb1\xbb\xe5\x9e\x8b', to='work.CoalType')),
                ('mine', models.ForeignKey(verbose_name=b'\xe5\x87\xba\xe5\x8f\x91\xe7\x85\xa4\xe7\x9f\xbf', to='work.Mine')),
                ('scale', models.ForeignKey(verbose_name=b'\xe5\x88\xb0\xe8\xbe\xbe\xe7\xa3\x85\xe6\x88\xbf', to='work.Scale')),
            ],
            options={
                'verbose_name': '\u8fd0\u8d39',
                'verbose_name_plural': '\u8fd0\u8d39',
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
                ('card_payed', models.BooleanField(default=False)),
                ('cash_payed', models.BooleanField(default=False)),
                ('card', models.ForeignKey(to='work.Card', null=True)),
                ('coal_type', models.ForeignKey(to='work.CoalType')),
                ('mine', models.ForeignKey(to='work.Mine')),
                ('scale', models.ForeignKey(to='work.Scale', null=True)),
            ],
            options={
                'permissions': (('mine', 'mine'), ('scale', 'scale'), ('account', 'account')),
            },
        ),
    ]
