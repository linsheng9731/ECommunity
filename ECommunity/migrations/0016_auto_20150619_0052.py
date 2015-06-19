# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ECommunity', '0015_auto_20150619_0014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='cata',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='type',
        ),
        migrations.AlterField(
            model_name='channel',
            name='content',
            field=models.TextField(verbose_name=b'\xe6\xad\xa3\xe6\x96\x87'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='image',
            field=models.ImageField(upload_to=b'', verbose_name=b'\xe7\xbc\xa9\xe7\x95\xa5\xe5\x9b\xbe'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='num',
            field=models.CharField(max_length=100, verbose_name=b'\xe7\x9b\xae\xe5\xbd\x95\xe9\xa1\xba\xe5\xba\x8f'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='image',
            field=models.ImageField(upload_to=b'', verbose_name=b'\xe7\xbc\xa9\xe7\x95\xa5\xe5\x9b\xbe'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='type',
            field=models.CharField(default=b'2', max_length=300, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
    ]
