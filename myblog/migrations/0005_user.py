# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 02:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=20)),
                ('nickName', models.CharField(max_length=20)),
                ('creatTime', models.DateTimeField()),
                ('latestLogin', models.DateTimeField()),
                ('status', models.CharField(max_length=1)),
                ('iconUrl', models.CharField(max_length=40)),
            ],
        ),
    ]