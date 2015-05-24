# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('img', models.CharField(max_length=100)),
                ('type', models.TextField()),
                ('create_time', models.CharField(max_length=100)),
                ('url', models.CharField(default=None, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=300)),
                ('img', models.CharField(max_length=300)),
                ('cata', models.CharField(max_length=100)),
                ('num', models.CharField(max_length=100)),
                ('dec', models.TextField()),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=300)),
                ('grade', models.CharField(max_length=100)),
                ('articles', models.ManyToManyField(to='ECommunity.Article')),
                ('channels', models.ManyToManyField(to='ECommunity.Channel')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='channel',
            field=models.ForeignKey(to='ECommunity.Channel'),
        ),
    ]
