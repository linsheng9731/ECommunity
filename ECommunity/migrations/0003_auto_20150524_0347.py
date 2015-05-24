# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ECommunity', '0002_auto_20150524_0219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='img',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='channel',
            old_name='img',
            new_name='image',
        ),
    ]
