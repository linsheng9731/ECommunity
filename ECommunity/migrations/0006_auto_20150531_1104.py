# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ECommunity', '0005_article_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='text',
            field=models.TextField(default=b'', verbose_name=b'\xe7\xba\xaf\xe6\x96\x87\xe6\x9c\xac'),
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=100, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85'),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(verbose_name=b'\xe6\xad\xa3\xe6\x96\x87'),
        ),
        migrations.AlterField(
            model_name='article',
            name='channel',
            field=models.ForeignKey(verbose_name=b'\xe9\xa2\x91\xe9\x81\x93', to='ECommunity.Channel'),
        ),
        migrations.AlterField(
            model_name='article',
            name='create_time',
            field=models.CharField(max_length=100, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='article',
            name='day',
            field=models.CharField(default=1, max_length=100, verbose_name=b'\xe5\x88\x86\xe9\xa1\xb5\xe5\x93\x9f\xe6\x80\x92'),
        ),
        migrations.AlterField(
            model_name='article',
            name='desc',
            field=models.TextField(default=b'', verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98\xe5\x9b\xbe'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='article',
            name='type',
            field=models.TextField(verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.CharField(default=None, max_length=300, verbose_name=b'\xe5\x88\x86\xe4\xba\xab\xe5\x9c\xb0\xe5\x9d\x80'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='cata',
            field=models.CharField(max_length=100, verbose_name=b'\xe4\xb8\x80\xe7\xba\xa7\xe7\x9b\xae\xe5\xbd\x95\xe9\xa1\xba\xe5\xba\x8f'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='content',
            field=models.CharField(max_length=300, verbose_name=b'\xe6\xad\xa3\xe6\x96\x87'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='desc',
            field=models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='image',
            field=models.CharField(max_length=300, verbose_name=b'\xe7\xbc\xa9\xe7\x95\xa5\xe5\x9b\xbe'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='num',
            field=models.CharField(max_length=100, verbose_name=b'\xe4\xba\x8c\xe7\xba\xa7\xe7\x9b\xae\xe5\xbd\x95\xe9\xa1\xba\xe5\xba\x8f'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='title',
            field=models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='type',
            field=models.CharField(max_length=100, verbose_name=b'0 \xe8\xa1\xa8\xe7\xa4\xba\xe4\xb8\x80\xe7\xba\xa7\xe7\x9b\xae\xe5\xbd\x95\xef\xbc\x8c1 \xe8\xa1\xa8\xe7\xa4\xba\xe4\xba\x8c\xe7\xba\xa7\xe7\x9b\xae\xe5\xbd\x95'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='articles',
            field=models.ManyToManyField(to='ECommunity.Article', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='channels',
            field=models.ManyToManyField(to='ECommunity.Channel', verbose_name=b'\xe9\xa2\x91\xe9\x81\x93'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='grade',
            field=models.CharField(max_length=100, verbose_name=b'\xe7\xa7\xaf\xe5\x88\x86'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='icon',
            field=models.CharField(max_length=300, verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='nickname',
            field=models.CharField(max_length=100, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=100, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d\xe5\x8f\xb7\xe7\xa0\x81'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='sex',
            field=models.CharField(max_length=100, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab'),
        ),
    ]
