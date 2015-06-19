# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ECommunity', '0013_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='create_time',
            field=models.DateTimeField(max_length=100, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='image',
            field=models.ImageField(upload_to=b'', max_length=300, verbose_name=b'\xe7\xbc\xa9\xe7\x95\xa5\xe5\x9b\xbe'),
        ),
    ]
