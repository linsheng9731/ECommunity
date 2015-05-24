# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ECommunity', '0003_auto_20150524_0347'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='desc',
            field=models.TextField(default=b''),
        ),
    ]
