# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ECommunity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='author',
            field=models.ManyToManyField(to='ECommunity.Customer', verbose_name=b'\xe7\xbc\x96\xe8\xbe\x91\xe4\xba\xba\xe5\x91\x98'),
        ),
    ]
