# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ECommunity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Article_author', models.CharField(max_length=100)),
                ('Article_Title', models.CharField(max_length=100)),
                ('Article_Body', models.TextField()),
                ('Article_Logo_pic', models.CharField(max_length=100)),
                ('Article_Desc', models.TextField()),
                ('Article_Create_time', models.CharField(max_length=100)),
                ('Article_Create_modify', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Channel_Name', models.CharField(max_length=100)),
                ('Type_ID', models.CharField(max_length=100)),
                ('Channel_Num', models.CharField(max_length=100)),
                ('Channel_Cata', models.CharField(max_length=100)),
                ('Channel_Desc', models.CharField(max_length=100)),
                ('Channel_PicURL', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('User_Phone', models.CharField(max_length=100)),
                ('User_NickName', models.CharField(max_length=100)),
                ('User_Sex', models.CharField(max_length=100)),
                ('User_PicURL', models.CharField(max_length=100)),
                ('User_Grade', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='article',
            name='Article_channel_ID',
            field=models.ForeignKey(to='ECommunity.Channel'),
        ),
    ]
