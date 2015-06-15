# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ECommunity', '0007_auto_20150613_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppSeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.CharField(max_length=100, verbose_name=b'\xe9\xa6\x96\xe9\xa1\xb5\xe5\x9b\xbe\xe7\x89\x87')),
            ],
        ),
    ]
