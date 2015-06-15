# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ECommunity', '0006_search'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='read_times',
            field=models.IntegerField(default=0, verbose_name=b'\xe9\x98\x85\xe8\xaf\xbb\xe6\xac\xa1\xe6\x95\xb0'),
        ),
        migrations.AlterField(
            model_name='search',
            name='keyword',
            field=models.CharField(max_length=30),
        ),
    ]
