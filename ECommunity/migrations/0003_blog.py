# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('ECommunity', '0002_auto_20150524_0219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=100, blank=True)),
                ('Content', DjangoUeditor.models.UEditorField(default=b'test', verbose_name='\u5185\u5bb9   ', blank=True)),
            ],
        ),
    ]
