# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ECommunity', '0004_auto_20150606_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='type',
            field=models.CharField(default=b'C', max_length=300, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
        migrations.AlterField(
            model_name='article',
            name='type',
            field=models.TextField(default=b'A', verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
    ]
