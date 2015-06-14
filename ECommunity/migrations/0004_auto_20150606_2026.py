# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ECommunity', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='channel',
            field=models.ForeignKey(default=1, verbose_name=b'\xe9\xa2\x91\xe9\x81\x93', to='ECommunity.Channel'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='articles',
            field=models.ManyToManyField(to='ECommunity.Article', verbose_name=b'article'),
        ),
        migrations.RemoveField(
            model_name='collection',
            name='author',
        ),
        migrations.AddField(
            model_name='collection',
            name='author',
            field=models.CharField(default=b'None', max_length=300),
        ),
        migrations.AlterField(
            model_name='customer',
            name='articles',
            field=models.ManyToManyField(to='ECommunity.Article', verbose_name=b'article'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='channels',
            field=models.ManyToManyField(to='ECommunity.Channel', verbose_name=b'channel'),
        ),
    ]
