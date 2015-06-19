# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ECommunity', '0016_auto_20150619_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='cata',
            field=models.CharField(default=b'0', max_length=100, verbose_name=b'\xe4\xb8\x80\xe7\xba\xa7\xe7\x9b\xae\xe5\xbd\x95\xe9\xa1\xba\xe5\xba\x8f'),
        ),
        migrations.AddField(
            model_name='channel',
            name='type',
            field=models.CharField(default=b'0', max_length=100, verbose_name=b'0 \xe8\xa1\xa8\xe7\xa4\xba\xe4\xb8\x80\xe7\xba\xa7\xe7\x9b\xae\xe5\xbd\x95\xef\xbc\x8c1 \xe8\xa1\xa8\xe7\xa4\xba\xe4\xba\x8c\xe7\xba\xa7\xe7\x9b\xae\xe5\xbd\x95'),
        ),
        migrations.AlterField(
            model_name='article',
            name='day',
            field=models.CharField(default=1, max_length=100, verbose_name=b'\xe5\x88\x86\xe9\xa1\xb5'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='content',
            field=models.CharField(max_length=300, verbose_name=b'\xe6\xad\xa3\xe6\x96\x87'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='num',
            field=models.CharField(max_length=100, verbose_name=b'\xe4\xba\x8c\xe7\xba\xa7\xe7\x9b\xae\xe5\xbd\x95\xe9\xa1\xba\xe5\xba\x8f'),
        ),
    ]
