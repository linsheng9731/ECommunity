# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ECommunity', '0005_auto_20150607_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='type',
            field=models.CharField(default=b'C', max_length=100, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
    ]
