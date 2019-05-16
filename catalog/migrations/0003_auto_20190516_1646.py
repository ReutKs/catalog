# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-16 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20190515_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('parent', models.IntegerField(default=0)),
                ('url', models.CharField(max_length=30)),
                ('image', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=30)),
                ('image', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Cpu',
        ),
        migrations.DeleteModel(
            name='Monitor',
        ),
    ]