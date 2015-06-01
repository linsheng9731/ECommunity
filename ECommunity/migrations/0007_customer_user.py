# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ECommunity', '0006_auto_20150531_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(default=1, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe6\x9d\x83\xe9\x99\x90', to=settings.AUTH_USER_MODEL),
        ),
    ]
