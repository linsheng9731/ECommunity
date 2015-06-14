# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ECommunity', '0008_record_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='customer',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
