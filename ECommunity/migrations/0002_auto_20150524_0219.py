# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ECommunity', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channel',
            old_name='dec',
            new_name='desc',
        ),
    ]
