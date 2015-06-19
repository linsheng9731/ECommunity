# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ECommunity', '0014_auto_20150618_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='create_time',
            field=models.CharField(max_length=100, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
