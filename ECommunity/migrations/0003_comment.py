# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ECommunity', '0002_collection_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('article', models.ForeignKey(to='ECommunity.Article')),
                ('customer', models.ForeignKey(to='ECommunity.Customer')),
            ],
        ),
    ]
