# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ECommunity', '0011_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='total_durations',
            field=models.CharField(default=b'0', max_length=500),
        ),
        migrations.AddField(
            model_name='customer',
            name='total_times',
            field=models.CharField(default=b'0', max_length=500),
        ),
        migrations.AddField(
            model_name='record',
            name='times',
            field=models.CharField(default=b'0', max_length=400),
        ),
    ]
