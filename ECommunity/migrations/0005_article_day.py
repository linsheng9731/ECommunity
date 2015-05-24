# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ECommunity', '0004_article_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='day',
            field=models.CharField(default=1, max_length=100),
        ),
    ]
