# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ECommunity', '0009_auto_20150614_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='customer',
            field=models.ForeignKey(default=4, to='ECommunity.Customer'),
        ),
    ]
