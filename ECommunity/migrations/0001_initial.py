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
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=100, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85')),
                ('title', models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('body', models.TextField(verbose_name=b'\xe6\xad\xa3\xe6\x96\x87')),
                ('text', models.TextField(default=b'', verbose_name=b'\xe7\xba\xaf\xe6\x96\x87\xe6\x9c\xac')),
                ('image', models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98\xe5\x9b\xbe')),
                ('type', models.TextField(verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('create_time', models.CharField(max_length=100, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('url', models.CharField(default=None, max_length=300, verbose_name=b'\xe5\x88\x86\xe4\xba\xab\xe5\x9c\xb0\xe5\x9d\x80')),
                ('desc', models.TextField(default=b'', verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('day', models.CharField(default=1, max_length=100, verbose_name=b'\xe5\x88\x86\xe9\xa1\xb5\xe5\x93\x9f\xe6\x80\x92')),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('content', models.CharField(max_length=300, verbose_name=b'\xe6\xad\xa3\xe6\x96\x87')),
                ('image', models.CharField(max_length=300, verbose_name=b'\xe7\xbc\xa9\xe7\x95\xa5\xe5\x9b\xbe')),
                ('cata', models.CharField(max_length=100, verbose_name=b'\xe4\xb8\x80\xe7\xba\xa7\xe7\x9b\xae\xe5\xbd\x95\xe9\xa1\xba\xe5\xba\x8f')),
                ('num', models.CharField(max_length=100, verbose_name=b'\xe4\xba\x8c\xe7\xba\xa7\xe7\x9b\xae\xe5\xbd\x95\xe9\xa1\xba\xe5\xba\x8f')),
                ('desc', models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('type', models.CharField(max_length=100, verbose_name=b'0 \xe8\xa1\xa8\xe7\xa4\xba\xe4\xb8\x80\xe7\xba\xa7\xe7\x9b\xae\xe5\xbd\x95\xef\xbc\x8c1 \xe8\xa1\xa8\xe7\xa4\xba\xe4\xba\x8c\xe7\xba\xa7\xe7\x9b\xae\xe5\xbd\x95')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('image', models.CharField(max_length=300, verbose_name=b'\xe7\xbc\xa9\xe7\x95\xa5\xe5\x9b\xbe')),
                ('desc', models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('create_time', models.CharField(max_length=100, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('articles', models.ManyToManyField(to='ECommunity.Article', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=100, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d\xe5\x8f\xb7\xe7\xa0\x81')),
                ('nickname', models.CharField(max_length=300, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0')),
                ('sex', models.CharField(max_length=100, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab')),
                ('icon', models.CharField(max_length=300, verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f')),
                ('grade', models.CharField(max_length=100, verbose_name=b'\xe7\xa7\xaf\xe5\x88\x86')),
                ('articles', models.ManyToManyField(to='ECommunity.Article', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0')),
                ('channels', models.ManyToManyField(to='ECommunity.Channel', verbose_name=b'\xe9\xa2\x91\xe9\x81\x93')),
                ('user', models.ForeignKey(default=1, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe6\x9d\x83\xe9\x99\x90', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='channel',
            field=models.ForeignKey(verbose_name=b'\xe9\xa2\x91\xe9\x81\x93', to='ECommunity.Channel'),
        ),
    ]
