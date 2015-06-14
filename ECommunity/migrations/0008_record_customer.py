# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ECommunity', '0007_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='customer',
            field=models.ForeignKey(default=7, to='ECommunity.Customer'),
        ),
    ]
